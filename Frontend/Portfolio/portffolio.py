import pandas as pd
import numpy as np
import os
import itertools

df=pd.read_csv('portfolioSymbol.csv')

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
    print(remaining)
    return y


amount=20000
time="Year"
add_industry(df,time)
df=create_data(df,time)
df=df.sort_values(by=time,ascending=False,ignore_index=True)
dict=csv_to_dict(df,time)
x,y=find_max_profit(dict,amount)
print(+x/8)
total_price = sum(stock[1] for stock in y)
y=quantity_check(amount,total_price,y)
print(y)
