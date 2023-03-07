import pandas as pd
import numpy as np
import streamlit as st
import yfinance as yf  # yahoo finance library to access stock price data
import datetime


st.image("./images/apple_logo.png",width=300)

# Heading of the page
st.write("""
# Stock Price Analyser

Shown are the apple stock's **closing prices** and **volume of share** traded

""")



 # 1. ticker symbol is the symbol given to companies register in stock
 #  e.g. 1. Relience ticker symbol :- REL
 #      2. HDFC :- HDFC
 #      3. Apple :- AAPL
 # 2. Date Period:- Period of which the data is required for prediction   



col1, col2 = st.columns(2)

# Adding date selection 
with col1: 
    start_date = st.date_input("Input Starting Date", datetime.date(2019, 1, 1))

with col2:
    end_date = st.date_input("Input Starting Date", datetime.date(2020, 1, 1))


ticker_symbol = "AAPL"
ticker_data = yf.Ticker(ticker_symbol)
ticker_df = ticker_data.history(period = "1d", start = f"{start_date}", end = f"{end_date}")

st.dataframe(ticker_df)

st.write('''
## Closing Price Chart
''')
st.line_chart(ticker_df.Close)

st.write('''
## Volume of Shares Traded
''')
st.line_chart(ticker_df.Volume)

# Adding expander to add terms and conditions
with st.expander("See explanation"):
    st.write("""
    This is a information of apple stock prices over period of time
    """ )
    st.image("./images/apple_logo.png",width=50)