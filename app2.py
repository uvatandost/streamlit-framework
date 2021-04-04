import requests
import pandas as pd
import streamlit as st
import numpy as np
import bokeh
from bokeh.plotting import figure
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import os
from dotenv import load_dotenv


"""
# TDI Milestone Project
An interactive chart of stock closing prices
"""

st.sidebar.write("Please enter a ticker and select a date range:")

project_folder = os.path.expanduser('C:/Users/uvata/Projects/streamlit-framework')
load_dotenv(os.path.join(project_folder, '.env'))
key = os.getenv("KEY")

# Input a ticker
ticker = str(st.sidebar.text_input('Ticker:', 'GOOG'))

# Fetching the data from API
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={}&apikey={}'.format(ticker, key)

try:
	@st.cache
	def load_data():
		response = requests.get(url)
		response = response.json()
		df = pd.DataFrame(response['Time Series (Daily)']).transpose()
		return df

	df = load_data()
	df.columns = ["open", "high", "low", "close", "adjusted close",
	" volume", "divident amount", "split coefficient"]

	df = df.applymap(float) # converting datapoints from str to float
	df = df.reindex(index=df.index[::-1])
	start_date, end_date = st.sidebar.select_slider('Date Range:',
	options=list(df.index),
	value=(df.index[0], df.index[99]))

	df = df[start_date:end_date]

	fig = px.line(df, x=df.index, y="close")
	fig.update_layout(title=str(ticker.upper()), xaxis_title='Date',yaxis_title='Closing Price')
	st.plotly_chart(fig, use_container_width=True)
except KeyError:
	st.write("Please enter a valid ticker (e.i. AAPL)")
else:
	pass
