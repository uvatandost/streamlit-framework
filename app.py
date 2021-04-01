import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
import seaborn as sns
import matplotlib.pyplot as plt
import plotly


"""
# How Do a Government's Democracy Qualities Influence Internal Conflicts in a Country?
"""
"\n",
"\n",
"\n",
st.write("Conflicts and wars seem to never end in the world we're livig in. This project is to perform an exploratory data analysis and visualization on the dataset provided by The Quality of Governments Institute to explore the relationship between some select government democracy qualities and conflict intensity in any given country. The analysis reveals a strong relationship between those democracy qualities and conflict intensity which helps explain why conflict is very common in some particular regions.")

# Adding a map of SF with some random sampled dots
np.random.seed(0)
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

data_source = "C:/Users/uvata/OneDrive/Documents/Harrisbug University/Analytics/Expl Data Analy (ANLY 506 51 B-2020Summer)/Final Project/qog_std_ts_jan20.csv"

@st.cache
def load_data():
    data = pd.read_csv(data_source, low_memory=False)
    return data

qog = load_data()
qog1 = qog[['cname', 'year', 'bti_ci', 'bti_seb', 'bti_si',
                      'bti_sop', 'bti_rol','bti_pp', 'bti_pdi',
                      'bti_ij', 'bti_foe', 'bti_ffe','bti_eo','bti_csp',
                      'bti_cr','bti_aod','bti_aar']]


qog2 = qog1.dropna()

# Input
country = st.sidebar.text_input('Enter a Country:', 'Albania')


country = qog2.loc[qog2.cname==country]
country.set_index("year", inplace=True)
country = country.drop("cname", axis=1)

# Checkbox
bti_ci = st.sidebar.checkbox('Conflict Intensity')
bti_seb = st.sidebar.checkbox('Socio-economic Barriers')
bti_ci = st.sidebar.checkbox('State Identity')
bti_ci = st.sidebar.checkbox('Separation of Powers')
country1 = country
if bti_ci:
	country1 = country[["bti_ci"]]
elif bti_ci and bti_seb:
	country1=country[["bti_ci","bti_seb"]]
#'country_name', 'conflict_intensity','socio_economic_barriers',
 #    'state_identity', 'separation_of_powers', 'rule_of_law', 
  #   'political_participation', 'perf_of_dem_inst', 'indep_judiciary',
   #  'freedom_of_express', 'free_fair_elec', 'equal_opp',
    # 'civil_soci_partic','civil_rights','associ_assembl_rights')

"In the expander below, you can see the original dataset along with a subset of it for a country you select on the left side panel."

with st.beta_expander("See the data"):
    "QoG Data",
    qog2,
    "\n",
    "\n",
    "Subset of data for selected country"
    country
    "\n",
    "\n",    

#st.write(country)
"\n"
"\n"
"\n"
# Line Chart
"Here you can pick and see changes over the years in any of the government qualities for the selected country"
st.line_chart(country1)

# Scatter plot

#plt.figure(figsize=(5,3))
#sns.lmplot(x="bti_csp", y="bti_ci", data=qog2)
#st.pyplot()
#st.set_option('deprecation.showPyplotGlobalUse', False)

# Age slider
st.sidebar.write("\n")
year = st.sidebar.slider('Slide to change the year', 2005, 2018, 2005)

#st.write("I'm ", age, 'years old')
year = qog2.loc[qog2["year"]==year]
year.set_index("cname", inplace=True)
year.drop('year', axis=1)

"\n"
# Multiselect options
options = st.sidebar.multiselect(
   'Pick measures',
   ['bti_seb', 'bti_si',
    'bti_sop', 'bti_rol','bti_pp', 'bti_pdi',
    'bti_ij', 'bti_foe', 'bti_ffe','bti_eo','bti_csp',
    'bti_cr','bti_aod','bti_aar'])

# plot

for item in options:

	sns.set_style('ticks')
	fig, ax = plt.subplots()
	fig.set_size_inches(4, 2)
	sns.regplot(x=item, y="bti_ci", data=year, ax=ax)
	sns.despine()
	st.pyplot()
	st.set_option('deprecation.showPyplotGlobalUse', False)

with st.beta_expander("See the data"):
    year




#sns.PairGrid(hue="bti_ci", # Grouping variable that will produce elements with different colors.
 #            data=year)
#st.pyplot()
#st.set_option('deprecation.showPyplotGlobalUse', False)

#sns.relplot(data=year, x=year.columns, y="bti_ci", col=year.columns, col_wrap=4)
#g = sns.FacetGrid(year, col=year.columns, height=4, col_wrap=4)
#g.map(sns.scatterplot(year), "bti_ci")
#st.pyplot()
#st.set_option('deprecation.showPyplotGlobalUse', False)

#sns.pairplot(hue="bti_ci", # Grouping variable that will produce elements with different colors.
 #            data=qog2)
#st.pyplot()
#st.set_option('deprecation.showPyplotGlobalUse', False)

# Age slider
#age = st.slider('How old are you?', 0, 130, 25)
#st.write("I'm ", age, 'years old')

# Range slider
#values = st.slider(
#    'Select a range of values',
#    0.0, 100.0, (25.0, 75.0))
#st.write('Values:', values)




# Creating a random dataframe
#df = pd.DataFrame({
#  'first column': [1, 2, 3, 4],
#  'second column': [10, 20, 30, 40]
#})

#df
#st.line_chart(df)

# Creating a bar chart for the above dataframe

#chart_data = pd.DataFrame(
#     np.random.randn(20, 3),
#     columns=['a', 'b', 'c'])




# Creating a line chart with a random dataframe
#chart_data = pd.DataFrame(
#     np.random.randn(20, 3),
#     columns=['a', 'b', 'c'])

#st.line_chart(chart_data) 





# Using a checkbox to show/hide data
#if st.checkbox('Show dataframe'):
#    chart_data = pd.DataFrame(
#       np.random.randn(20, 3),
#       columns=['a', 'b', 'c'])

 #   st.line_chart(chart_data)


# Useinf selectbox for options, a dropdown menu
#option = st.selectbox(
#    'Which number do you like best?',
#     df['first column'])

#'You selected: ', option


# Laying out the app, moving the selectbox to leftside
#option = st.sidebar.selectbox(
#    'Which number do you like best?',
#     df['first column'])

#'You selected:', option


# Some cool features like a button and an expander
#left_column, right_column = st.beta_columns(2)
#pressed = left_column.button('Press me?')
#if pressed:
#    right_column.write("You will explode in 10 seconds.")

#expander = st.beta_expander("FAQ")
#expander.write("Here you could put in some really, really long explanations...")


# Adding time
#import time

#'Starting a long computation...'

# Add a placeholder
#latest_iteration = st.empty()
#bar = st.progress(0)

#for i in range(100):
  # Update the progress bar with each iteration.
 # latest_iteration.text(f'Iteration {i+1}')
  #bar.progress(i + 1)
  #time.sleep(0.1)

#'...and now we\'re done!'
