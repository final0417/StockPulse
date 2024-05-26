import streamlit as st
import os
import pandas as pd
import requests
import time

import yfinance as yf

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

def app():
    col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11 = st.columns([10, 1, 1, 1, 1, 3, 1, 1, 1, 1, 3])
    with col1:
        st.markdown('<h1 style="color: #00ffff;">🔎 Explore </h1>', unsafe_allow_html=True)
    with col11:
        st.markdown('<style>img {border-radius: 200px;}</style>', unsafe_allow_html=True)
        st.image("dp.jpg", width=50)
    st.markdown("""---""")
    st.markdown('<h2 style="color: #ffa31a;">📊 Top Stocks in India </h2>', unsafe_allow_html=True)
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.success("NIFTY Automobiles")
        worth=get_share_price('^CNXAUTO')
        st.metric(label="Rs", value=round(worth, 2))
    with col2:
        st.success("NIFTY Bank")
        worth=get_share_price('^NSEBANK')
        st.metric(label="Rs", value=round(worth, 2))
    with col3:
        st.success("NIFTY IT")
        worth=get_share_price('^CNXIT')
        st.metric(label="Rs", value=round(worth, 2))
    with col4:
        st.error("NIFTY Food")
        worth=get_share_price('^NSEI')
        st.metric(label="Rs", value=round(worth, 2))
    with col5:
        st.success("NIFTY Metal")
        worth=get_share_price('^CNXMETAL')
        st.metric(label="Rs", value=round(worth, 2))
    st.markdown("""---""")
    col1,col2,col3=st.columns([5,1,1])
    with col1:
        st.markdown('<h2 style="color: #ffa31a;">📰🗞️ Top Stock News IN India  </h2>', unsafe_allow_html=True)
    with col3:
        st.markdown('<h3 style="color: #00ffff;">🔎</h3>', unsafe_allow_html=True)
    with st.form(key='form1'):
        url = "https://news.google.com/rss/search?q=indian%20stock%20market&hl=en-IN&gl=IN&ceid=IN:en"
        response = requests.get(url)
        if response.status_code == 200:
            rss_feed = response.text
            articles = []
            items = rss_feed.split("<item>")[1:]
            for item in items:
                headline = item.split("<title>")[1].split("</title>")[0]
                link = item.split("<link>")[1].split("</link>")[0]
                st.markdown(f"<h4>📰 {headline}</h4>",unsafe_allow_html=True)
                link_text = "see more.."
                st.markdown(f"[{link_text}]({link})")
                st.markdown("""---""")
        submit_button = st.form_submit_button(label='Show More News')