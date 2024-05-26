import numpy as np
import pandas as pd
import statsmodels.api as sm
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
from numpy import array
from keras.models import Sequential
from keras.layers import Dense,Flatten
from tensorflow.python.keras.layers import LSTM
import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from datetime import datetime, timedelta
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import RandomizedSearchCV
from datetime import datetime, timedelta
import statsmodels.api as sm
from statsmodels.tsa.stattools import adfuller
import time
import schedule

def read(s):
    df=pd.read_csv(s)
    return df

def increase(date_string):
    date_obj = datetime.strptime(date_string, "%Y-%m-%d")
    new_date_obj = date_obj + timedelta(days=1)
    formatted_date = datetime.strftime(new_date_obj, "%Y-%m-%d")
    return formatted_date

def fillup(df):
    x=df['Date'].iloc[-1]
    start_date=df['Date'][0]
    new_df=pd.DataFrame()
    end_date=x
    date_index = pd.date_range(start=start_date, end=end_date, freq='D')
    new_df['Date']=date_index
    df['Date'] = pd.to_datetime(df['Date'])
    merged_df = pd.merge(df,new_df, on='Date', how='right')
    merged_df=merged_df.interpolate(method='ffill',limit_direction='forward')
    return merged_df

def test(df,index):
    x=df[index].values
    result=adfuller(x)
    if(result[1] >0.05 and result[0]>result[4]['1%'] and result[0]>result[4]['5%'] and result[0]>result[4]['10%']):
        return 0
    else:
        return 1

def adf(df,index):
    if(test(df,index)==0):
        df['Value']=df[index].diff()
        x=df['Value'].mean()
        df['Value']=df['Value'].fillna(x)
        df=adf(df,'Value')
    return df

def minimize(df):
    data=pd.DataFrame()
    data['Date']=df['Date']
    data['Original']=df['Close']
    data['Value']=df['Value']
    return data

def xerox(df):
    df1=pd.DataFrame()
    df1['Date']=df['Date']
    df1['Original']=df['Original']
    df1['Value']=df['Value']
    return df1

def split_sequence(sequence,steps):
    x,y=list(),list()
    for start in range(len(sequence)):
        end_index=start+steps
        if end_index > len(sequence)-1:
            break;
        sequence_x,sequence_y=sequence[start:end_index],sequence[end_index]
        x.append(sequence_x)
        y.append(sequence_y)
    return array(x),array(y)

def lstm_fun(df1):
    d=df1['Value'].tolist()
    steps=6
    x,y=split_sequence(d,steps)
    features=1
    x=x.reshape((x.shape[0],x.shape[1],features))
    #Build LSTM model
    model_lstm=Sequential()
    #Add first layer to model
    model_lstm.add(LSTM(50, return_sequences=True, input_shape=(x.shape[1],1)))
    #Add second layer to model
    model_lstm.add(LSTM(50, return_sequences=False))
    #Add Dense Layer to model with 25 neurons
    model_lstm.add(Dense(25))
    #Add Dense Layer to model with 1 neuron
    model_lstm.add(Dense(1))
    model_lstm.compile(loss='mean_squared_error',optimizer='adam')
    if(df1.shape[0]<=500):
        e=500
    elif(df1.shape[0]<=1500):
        e=1000
    else:
        e=2000
    model_lstm.fit(x,y,epochs=e,verbose=0)
    return model_lstm

def lstm_run(model_lstm,df1):
    d=df1['Value'].tolist()
    steps=6
    x,y=split_sequence(d,steps)
    test_data_x= x[-50:]
    test_data_y= y[-50:]

    test_data_pred=model_lstm.predict(test_data_x)
    """ mean = np.mean(test_data_pred)
    abs_deviations = np.abs(test_data_pred-mean)
    mad = np.mean(abs_deviations)
    #print("MAD:", mad)
    mse = mean_squared_error(test_data_y,test_data_pred)
    rmse = np.sqrt(mse)
    #print("RMSE :",rmse)
    def mean_absolute_percentage_error(y_actual, y_predicted):
        return np.mean(np.abs((y_actual-y_predicted)/y_actual))*100

    mape = mean_absolute_percentage_error(np.array(test_data_y), np.array(test_data_pred))
    #print("MAPE:", mape)


    def mean_bias_error(y_actual, y_predicted):
        return mean_squared_error(y_actual,y_predicted)

    mbe = mean_bias_error(np.array(test_data_y), np.array(test_data_pred))
    #print("MSE:", mbe)
    print(r2_score(test_data_y,test_data_pred))"""

def starting_date(df1):
    x=df1['Date'].iloc[-1]
    y = x.strftime('%Y-%m-%d')
    return y


def lstm_output(model_lstm, df1):
    d = df1['Value'].tolist()
    steps = 6
    x, y = split_sequence(d, steps)
    test_data_x = x[-50:]
    test_data_y = y[-50:]
    data = df1['Value'].tolist()
    forecasted_df = pd.DataFrame(columns=['Date', 'Value'])
    start_date = starting_date(df1)
    steps = 6
    features = 1
    model_lstm = lstm_fun(df1)
    for i in range(10):
        new_date = increase(start_date)
        forecast_input = array(data[-6:])
        x_forecast = forecast_input.reshape(1, steps, features)
        forecasted_y = model_lstm.predict(x_forecast).item()
        forecasted_df.at[i, 'Date'] = new_date
        forecasted_df.at[i, 'Value'] = forecasted_y
        data.append(forecasted_y)
        start_date = new_date

    index_old = np.arange(1, 51)
    index_new = np.arange(51, 61)

    """plt.plot(index_old, test_data_y, color='red')
    plt.plot(index_new,forecasted_df['Value'], color='green')"""

    forcasted_dif = forecasted_df['Value']
    dif_list = np.array(forcasted_dif).flatten().tolist()
    last_value = df1.tail(1)['Original'].iloc[0]

    forecasted_og = []

    for i in range(len(dif_list)):
        n = last_value + dif_list[i]
        forecasted_og.append(n)
        last_value = n

    forecasted_df['Retrive'] = forecasted_og

    index_old = np.arange(1, 51)
    index_new = np.arange(51, 61)

    last_300 = df1['Original'][-50:].tolist()

    """plt.plot(index_old, last_300, color='red')
    plt.plot(index_new,forecasted_df['Retrive'], color='green')"""
    return forecasted_df['Retrive']

def rfr_fun(df2):
    df2['Value']=scaler.fit_transform(df2[['Value']])
    data=df2['Value'].tolist()
    steps=6
    n=100
    ans=0
    max_acc=0
    while(n<=2000):
        x,y=split_sequence(data,steps)
        model=RandomForestRegressor(n_estimators=n, random_state = 42)
        model.fit(x,y)
        test_data_x= x[-50:]
        test_data_y= y[-50:]
        test_data_pred=model.predict(test_data_x)
        acc=r2_score(test_data_y,test_data_pred)
        if(acc>max_acc):
            max_acc=acc
            ans=n
        n=n+100
    model=RandomForestRegressor(n_estimators =ans, random_state = 42)
    model.fit(x,y)
    return model

def rfr_run(model,df2):
    d=df2['Value'].tolist()
    steps=6
    n=100
    ans=0
    max_acc=0
    x,y=split_sequence(d,steps)
    test_data_x= x[-50:]
    test_data_y= y[-50:]

    test_data_pred=model.predict(test_data_x)

    """"mean = np.mean(test_data_pred)
    abs_deviations = np.abs(test_data_pred-mean)
    mad = np.mean(abs_deviations)
    print("MAD:", mad)

    mse = mean_squared_error(test_data_y,test_data_pred)
    rmse = np.sqrt(mse)
    print("RMSE :",rmse)


    def mean_absolute_percentage_error(y_actual, y_predicted):
        return np.mean(np.abs((y_actual-y_predicted)/y_actual))*100

    mape = mean_absolute_percentage_error(np.array(test_data_y), np.array(test_data_pred))
    print("MAPE:", mape)


    def mean_bias_error(y_actual, y_predicted):
        return mean_squared_error(y_actual,y_predicted)

    mbe = mean_bias_error(np.array(test_data_y), np.array(test_data_pred))
    print("MSE:", mbe)

    print(r2_score(test_data_y,test_data_pred))"""

def rfr_output(model,df2):
    data=df2['Value'].tolist()
    forecasted_df=pd.DataFrame(columns=['Date','Value'])
    start_date=starting_date(df2)
    d=df2['Value'].tolist()
    steps=6
    x,y=split_sequence(d,steps)
    test_data_x= x[-50:]
    test_data_y= y[-50:]
    for i in range(10):
        new_date=increase(start_date)
        forecast_input=array(data[-6:])
        #x_forecast=forecast_input.reshape(1,steps,features) #lstm
        x_forecast=forecast_input.reshape(1,-1)
        forecasted_y=model.predict(x_forecast).item()
        forecasted_df.at[i,'Date']=new_date
        forecasted_df.at[i,'Value']=forecasted_y
        data.append(forecasted_y)
        start_date=new_date

    index_old=np.arange(1,51)
    index_new=np.arange(51,61)

    """lt.plot(index_old, test_data_y, color='red')
    plt.plot(index_new,forecasted_df['Value'], color='green')"""
    forcasted_dif=scaler.inverse_transform(np.array(forecasted_df['Value']).reshape(-1,1))
    dif_list=np.array(forcasted_dif).flatten().tolist()
    last_value=df2.tail(1)['Original'].iloc[0]

    forecasted_og=[]

    for i in range(len(dif_list)):
        n=last_value+dif_list[i]
        forecasted_og.append(n)
        last_value=n

    forecasted_df['Retrive']=forecasted_og

    index_old=np.arange(1,51)
    index_new=np.arange(51,61)

    last_300 = df2['Original'][-50:].tolist()

    """plt.plot(index_old, last_300, color='red')
    plt.plot(index_new,forecasted_df['Retrive'], color='green')"""
    return forecasted_df['Retrive']

def output(retrive_lstm,retrive_rfr):
    result=[]
    for i in range(len(retrive_rfr)):
        result.append(retrive_lstm[i]*0.6 + retrive_rfr[i]*0.4)
    return result

def final_plot(df,op):
    index_old=np.arange(1,51)
    index_new=np.arange(51,61)
    last_300 = df['Original'][-50:].tolist()
    plt.plot(index_old, last_300, color='red')
    plt.plot(index_new,op, color='green')

def auto():
    s='data.csv'
    df=read(s)
    df=fillup(df)
    #plt.plot(df['Close'])
    df=adf(df,'Close')
    #df.head()
    df=minimize(df)
    #df.head()
    df1=xerox(df)
    df2=xerox(df)
    model_lstm=lstm_fun(df1)
    lstm_run(model_lstm,df1)
    retrive_lstm=lstm_output(model_lstm,df1)
    model_rfr=rfr_fun(df2)
    rfr_run(model_rfr,df2)
    retrive_rfr=rfr_output(model_rfr,df2)
    op=output(retrive_lstm,retrive_rfr)
    final_plot(df,op)
    op

if __name__ == "__main__":
    scaler = MinMaxScaler()
    schedule.every().day.at("15:35").do(auto)
    while True:
        schedule.run_pending()
        time.sleep(3600)
