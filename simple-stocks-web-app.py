import yfinance as yf #library which provides an interface to fetch stock data from Yahoo Finance
import streamlit as st #library or framework for building interactive web applications 


st.title("Simple Stock Price App")


st.write("Shown are the **Closing Price** and **Volume** of Microsoft.")



#defining ticker symbol
tickerSymbol = 'MSFT'

#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

#get the historical prices for this sticker
tickerDf = tickerData.history(period = '1d', start = '2019-5-31', end = '2022-5-31')

#Open High Low Close Volume Dividends Stock Splits

st.write("""
## Closing Price

""")

#Generating line chart showing the closing prices over time, using the 'Close' column of the 'tickerDf' Dataframe
st.line_chart(tickerDf.Close)

#Subheading for the volume section
##Volume in stocks is the amount of stocks traded per period. 
st.write("""

## Volume Price
""")

#Generating line chart showing the volume of trades over time, using the 'volume' column of 'tickerDf' dataframe
st.line_chart(tickerDf.Volume)

