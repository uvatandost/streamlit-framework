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

project_folder = os.path.expanduser('C:/Users/uvata/Projects/streamlit-framework')  # adjust as appropriate
load_dotenv(os.path.join(project_folder, '.env'))
key = os.getenv("KEY")

#st.write(key)
#st.write(os.environ.get('KEY'))
#st.write(os.environ['HOME'])
#st.write(os.environ)

ticker = 'AAP'
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={}&apikey={}'.format(ticker, key)
response = requests.get(url)
response = response.json()
#print(response)


df = pd.DataFrame(response['Time Series (Daily)']).transpose()
df.columns = ["open", "high", "low", "close", "adjusted close",
" volume", "divident amount", "split coefficient"]

df = df.applymap(float) # converting datapoints from str to float
df = df.reindex(index=df.index[::-1])
st.write(df)
df2 = df.iloc[:20]['close']
'''
p = figure(title= "Closing Price",x_axis_label='Date',x_axis_type='datetime')
x = df.index
y = df.close
#x = np.arange(0,10)
p.line(x, y, legend_label=ticker, line_width=2)
st.bokeh_chart(p, use_container_width=False)
'''


fig = px.line(df, x=df.index, y="close")
st.plotly_chart(fig, use_container_width=True)


'''
sns.set_style('ticks')
fig, ax = plt.subplots()
fig.set_size_inches(4, 2)
x = df.index[0:8]
y = df.close
sns.lineplot(df, x=x, y=y)
st.pyplot()
'''
'''
st.line_chart(df2, use_container_width=True, height=300)

x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

p = figure(
	title='simple line example',
	x_axis_label='x',
	y_axis_label='y')

p.line(x, y, legend_label='Trend', line_width=2)
st.bokeh_chart(p)
show(p)
'''