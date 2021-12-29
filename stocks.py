import yfinance as yf
import streamlit as st
import pandas as pd

st.title("Stock Price Analysis")

scrip = st.text_input("Enter Script Name: ")
period = st.slider('Pick range', 1, 10)
startdate = st.date_input('Start Date(YYYY-M-DD)')
enddate = st.date_input('End Date(YYYY-M-DD)')
#print(str(period)+'d')
#tikerSymbol = 'GOOGL'
tickerData = yf.Ticker(scrip)
tickerDF = tickerData.history(period=str(period)+'d', start = startdate , end = enddate)

st.line_chart(tickerDF.Close)
st.line_chart(tickerDF.Volume)



