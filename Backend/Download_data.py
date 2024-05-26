import yfinance as yf
import pandas as pd

# Define the stock symbols
stocks = ["JTEKTINDIA.NS","PRICOLLTD.NS","JKTYRE.BO"]

# Fetching data for each stock
for stock_symbol in stocks:
    stock_data = yf.download(stock_symbol, start="2023-01-01", end="2024-01-01")
    
    # Save data to CSV
    filename = f"{stock_symbol}_data.csv"
    stock_data.to_csv(filename)
    print(f"Saved data for {stock_symbol} to {filename}")
