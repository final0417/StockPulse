import streamlit as st
import os
import pandas as pd
import itertools
import yfinance as yf
import ast

df=pd.read_csv('portfolioSymbol.csv')

def update_metrics(m1,m2,m3,x,y,z):
    m1.metric("Number",x)
    m2.metric("Rs",round(y,2))
    m3.metric("Rs",z)

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
    print(user_id)

    data_profiles = pd.read_csv('profile.csv')
    user = data_profiles[data_profiles['ID'] == user_id]

    portfolio_number = int(user['Portfolio_No'].values[0])
    total = round(float(user['Exp'].values[0]), 2)
    remaining = round(float(user['Amount'].values[0]), 2)
    tree = pd.read_csv('form.csv')
    data1 = pd.read_csv('company_s.csv')


    col1,col2,col3,col4,col5,col6,col7,col8,col9,col10,col11=st.columns([5,1,1,1,1,3,1,1,1,1,3])
    with col1:
        st.markdown('<h1 style="color: #00ffff;">💎 Premium</h1>', unsafe_allow_html=True)
    with col11:
        st.markdown('<style>img {border-radius: 200px;}</style>', unsafe_allow_html=True)
        st.image("dp.jpg", width=50)
    st.markdown("""---""")

    st.header("Create Your Stock Portfolio with our AI")
    st.markdown('''The whole Portfolio will be generated automatically based on Small Cap Stocks''')

    col1,col2,col3=st.columns(3)
    with col1:
        st.info("📊 Portfolios")
        metric1=st.metric(label="Number",value=portfolio_number)
    with col2:
        st.success("💵 Total Investment")
        metric2=st.metric(label="Rs.",value=round(total,2))
    with col3:
        st.warning("🪙 Amount Remaining")
        metric3=st.metric(label="Rs.",value=remaining)

    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1.3,1,1])
    with col2:
        st.button("Add Money")

    st.markdown('''---''')

    st.markdown('<h4 style="color: yellow;">Want to create a new Portfolio</h4>', unsafe_allow_html=True)

    with st.form(key='form1'):
        col1, col2 = st.columns(2)
        with col1:
            amount=st.number_input("Enter the Amount You want to Invest (Minimum Rs-1000) :",min_value=1000.00,max_value=remaining,key=float)
            if amount<500:
                st.error("Minimum Rs-500 should be invested")
        with col2:
            value=st.select_slider("How Much Risk You Want :",options=["Low","Low","Low","Low","High","High","High","High"])
        col1,col2=st.columns(2)
        with col1:
            selected_value = st.selectbox("Select how You want it to buy",["Market Price","Limit Price","SIP"])
        with col2:
            unique_id=st.text_input("Enter your PAN number to confirm: ")
        col1, col2, col3 = st.columns([2, 2, 2])
        with col2:
            tc=st.checkbox("I agree to the terms and conditions")
        st.markdown("<br>", unsafe_allow_html=True)
        col1,col2,col3 = st.columns([2.5,2,2])
        with col2:
            submit_form=st.form_submit_button(label="Create Portfolio")
        if submit_form:
            if tc and amount and unique_id and selected_value:
                col1, col2, col3 = st.columns([1.5, 2, 2])
                with col2:
                    st.success("Process Initiated... Go to Porfolio Page to check your updates")
            elif amount and unique_id and selected_value:
                col1, col2, col3 = st.columns([1.5, 2, 2])
                with col2:
                    st.warning("Please check Terms and Conditions")
            else:
                col1, col2, col3 = st.columns([1.3, 2, 2])
                with col2:
                    st.error("Please Fill the Form Properly")
            new_row = {"Amount": amount, 'Risk': value}
            tree=tree.append(new_row, ignore_index=True)
            tree.to_csv('form.csv',index=False)

            data_login = pd.read_csv('login.csv')
            user_id = data_login['ID'].iloc[-1]

            data_profiles = pd.read_csv('profile.csv')
            user = data_profiles[data_profiles['ID'] == user_id]

            expense = round(float(user['Exp'].values[0]), 2)

            tree = pd.read_csv('form.csv')
            form_amount = tree['Amount'].iloc[-1]
            form_value = tree['Risk'].iloc[-1]

            total, y = working(df, form_amount, form_value)
            worth = 0.0
            for i in y:
                s_p = data1[data1['Symbol'] == i[0]]
                s_price = s_p['Price'].iloc[0]
                worth = worth + (s_price * i[3])


            portfolio_number = portfolio_number + 1
            exepense=expense+total
            remaining = round(remaining - total, 2)

            index = "Portfolio" + str(portfolio_number)
            y = str(y)
            data_profiles.loc[data_profiles['ID'] == user_id, [index]] = [y]
            data_profiles.loc[data_profiles['ID'] == user_id, ['Portfolio_No', 'Exp','Amount']] = [portfolio_number, exepense,remaining]
            data_profiles.to_csv('profile.csv', index=False)

            update_metrics(metric1,metric2,metric3,portfolio_number, exepense, remaining)
