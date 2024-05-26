import streamlit as st
import pandas as pd
import time
import matplotlib.pyplot as plt
import os
import itertools
import yfinance as yf
import ast

def update_metric(worth):
    st.session_state.metric_value = worth

def add_industry(df,time):
    for i in df.columns:
        folder_name=i
        s=i+"_output_"+time+".csv"
        file=os.path.join(folder_name,s)
        data=pd.read_csv(file)
        data["Industry"]=i
        data.to_csv(file,index=False)

def csv_to_dict(df,time):
    data_dict = {}
    for index, row in df.iterrows():
        industry = row['Industry']
        name = row['Name']
        price = float(row['Price'])
        profit = float(row[time])
        if industry in data_dict:
            data_dict[industry].append([name,price,profit,1])
        else:
            data_dict[industry] = [[name,price,profit,1]]
    return data_dict

def create_data(df,time):
    list=[]
    for i in df.columns:
        folder_name=i
        s=i+"_output_"+time+".csv"
        file=os.path.join(folder_name,s)
        list.append(file)

    dfs=[]
    for file in list:
        di=pd.read_csv(file)
        dfs.append(di)
    combined_df=pd.concat(dfs, ignore_index=True)
    return combined_df

def graph_plot(data,time):
    data=data.tail(time)
    first_element = data['Value'].iloc[0]
    last_element = data['Value'].iloc[-1]
    #print(first_element, " ", last_element)
    if (first_element <= last_element):
        col = "green"
    else:
        col = "red"
    data['Date'] = pd.to_datetime(data['Date'])
    fig, ax = plt.subplots(figsize=(10,3))
    ax.plot(data['Date'], data['Value'], color=col)
    ax.set_facecolor('black')
    ax.tick_params(axis='y', colors='blue', labelsize=8)
    ax.set_xticks([])
    plt.xlabel('Date', color='white',fontsize=15)
    plt.ylabel('Value', color='white',fontsize=15)
    plt.savefig("plot.png", transparent=True)

def find_max_profit(stocks_data, budget):
    max_profit = 0
    selected_stocks = None

    # Generate combinations of stocks, one from each industry
    combinations = itertools.product(*stocks_data.values())

    for combination in combinations:
        total_price = sum(stock[1] for stock in combination)
        if total_price <= budget:
            total_profit = sum(stock[2] for stock in combination)
            if total_profit > max_profit:
                max_profit = total_profit
                selected_stocks = combination
    return max_profit, selected_stocks

def quantity_check(amount,invsetment,y):
    remaining=amount-invsetment
    while (remaining >= invsetment):
        for i in y:
            i[3]=i[3]+1
            remaining=remaining-i[1]
    least_cost=999999
    for i in y:
        least_cost=min(least_cost,i[1])
    while(remaining>=least_cost):
        for i in y:
            if remaining>=i[1]:
                i[3] = i[3] + 1
                remaining = remaining - i[1]
    total=amount-remaining
    return total,y

def get_share_price(symbol):
    try:
        # Get stock data
        stock = yf.Ticker(symbol)
        # Get the latest price
        latest_price = stock.history(period='1d')['Close'].iloc[-1]
        latest_price=round(latest_price,2)
        return latest_price
    except Exception as e:
        print("Error:", e)
        return None

def duration(x):
    if(x=="Low"):
        return "Day"
    else:
        return "Year"

def working(df,form_amount,form_value):
    amount=form_amount
    time=duration(form_value)
    add_industry(df,time)
    df=create_data(df,time)
    df=df.sort_values(by=time,ascending=False,ignore_index=True)
    dict=csv_to_dict(df,time)
    x,y=find_max_profit(dict,amount)
    total_price = sum(stock[1] for stock in y)
    total,y=quantity_check(amount,total_price,y)
    return total,y

def app():
    data_login = pd.read_csv('login.csv')
    user_id = data_login['ID'].iloc[-1]

    data_profiles = pd.read_csv('profile.csv')
    user = data_profiles[data_profiles['ID'] == user_id]

    portfolio_number = int(user['Portfolio_No'].values[0])
    total = round(float(user['Exp'].values[0]),2)

    tree=pd.read_csv('form.csv')
    form_amount = tree['Amount'].iloc[-1]
    form_value = tree['Risk'].iloc[-1]

    data1=pd.read_csv('company_s.csv')
    df = pd.read_csv('portfolioSymbol.csv')
    col1, col2, col3, col4, col5, col6, col7 = st.columns([10, 1, 1, 1, 1, 1, 3])
    with col1:
        st.markdown('<h1 style="color: #00ffff;">📊 Your PortFolios</h1>', unsafe_allow_html=True)
    with col7:
        st.markdown('<style>img {border-radius: 200px;}</style>', unsafe_allow_html=True)
        st.image("dp.jpg", width=50)
    st.markdown("Our Advanced algorithms have created this portfolio of small-cap stocks based on your selections, allowing you to maximise returns with minimal risk.")
    st.markdown("""---""")
    worth=0.0
    for u in range(1,portfolio_number+1):
        stri = "Portfolio" + str(u)
        matching_row = data_profiles.loc[data_profiles['ID'] == user_id]
        column_to_print = stri
        string_list = matching_row[column_to_print].values[0]
        actual_list = ast.literal_eval(string_list)
        for i in actual_list:
            s_p = data1[data1['Symbol'] == i[0]]
            s_price = s_p['Price'].iloc[0]
            worth = worth + (s_price * i[3])
    col1, col2, col3 = st.columns([1,1,1])
    with col1:
        st.info("🪙 All Your Assets Worth")
        m1=st.metric(label="Rs", value=round(worth,2))
    with col2:
        st.warning("💵 Investmented Amount")
        st.metric(label="Rs.", value=round(total,2))
    with col3:
        x=worth-total
        x=round(x,2)
        if(x>0.0):
            st.success("➡ Total Returns")
        else:
            st.error("Today's returns")
        st.metric(label="Rs.", value=x)
    st.markdown('''---''')
    st.subheader("Your Portfolio's Growth: ")
    data=pd.read_csv('graph.csv')
    col1, col2, col3 = st.columns(3)
    with col2:
        value = st.select_slider("How Much Risk You Want :",options=["1D","1W","1M","1Y","MAX"],value="1M")
        if value=="1D":
            x=2
        elif value=="1W":
            x=7
        elif value=="1M":
            x=30
        else:
            x=data.shape[0]
    col1, col2, col3=st.columns([0.3,2,1])
    with col2:
        graph_plot(data,x)
        st.image("plot.png",width=1000)
    if "previous_value" not in st.session_state:
        st.session_state.previous_value="1M"
    if st.session_state.previous_value != value:
        graph_plot(data,x)
        st.session_state.previous_value=value
    st.markdown('''---''')
    col1, col2, col3, col4, col5, col6, col7 = st.columns([3, 1, 1, 1, 1, 1, 1])
    with col1:
        st.header("Your Investments")
    with col7:
        st.markdown("<h3 style='text-align: center;'>🔍</h3>",unsafe_allow_html=True)

    data1=pd.read_csv('company_s.csv')


    matching_row = data_profiles.loc[data_profiles['ID'] == user_id]
    if not matching_row['Portfolio1'].isnull().all():
        st.markdown('<h1 style="color: yellow;">Here are Your Portfolios</h1>', unsafe_allow_html=True)
        portfolios = []
        for u in range(1, portfolio_number + 1):
            stri = "Portfolio" + str(u)
            portfolios.append(stri)
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            stri = st.selectbox("Select your Portfolio to see", portfolios)

        # stri="Portfolio"+str(u)
        matching_row = data_profiles.loc[data_profiles['ID'] == user_id]
        column_to_print = stri
        string_list = matching_row[column_to_print].values[0]
        actual_list = ast.literal_eval(string_list)
        st.subheader(f"{stri}")
        col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
        with col1:
            st.info("Company Name: ")
        with col2:
            st.warning("Quantity")
        with col3:
            st.success("Current Price")
        with col4:
            st.error("Purchase Price")
        for i in actual_list:
            col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
            s = i[0]
            result = data1[data1['Symbol'] == s]
            if not result.empty:
                price = result['Price'].iloc[0]
                name = result['Company'].iloc[0]
            with col1:
                st.write(name)
            with col2:
                st.write(f"<span style='color:yellow'>{i[3]}</span>", unsafe_allow_html=True)
            with col3:
                if price < round(i[1]):
                    st.write(f"<span style='color:red'>{price}</span>", unsafe_allow_html=True)
                else:
                    st.write(f"<span style='color:green'>{price}</span>", unsafe_allow_html=True)
            with col4:
                if price < round(i[1]):
                    st.write(f"<span style='color:orange'>{round(i[1], 2)}</span>", unsafe_allow_html=True)
                else:
                    st.write(f"<span style='color:red'>{round(i[1], 2)}</span>", unsafe_allow_html=True)

            update_metric(worth)

    data_profiles.to_csv('profile.csv', index=False)