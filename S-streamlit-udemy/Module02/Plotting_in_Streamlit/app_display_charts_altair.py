# Core Pkgs
import streamlit as st 

# Load EDA Pkgs
import pandas as pd 
import numpy as np

# Import Altair
import altair as alt



def main():
	st.title("Plotting In Streamlit")
	# Load Dataset
	# df = pd.read_csv("data/iris.csv")
	df2 = pd.read_csv("data/lang_data.csv")
	st.dataframe(df2.head())

	# Bar Chart
	# Using St.bar_chart
	# st.bar_chart(df[['sepal_length','petal_length']])

	# Line Chart
	lang_list = df2.columns.tolist()
	lang_choices = st.multiselect("Choose Language",lang_list,default='Python')
	new_df = df2[lang_choices]
	st.line_chart(new_df)

	# Area Chart
	st.area_chart(new_df,use_container_width=True)

	# Altair 
	df = pd.DataFrame(
	np.random.randn(200, 3),
	columns=['a', 'b', 'c'])
	c = alt.Chart(df).mark_circle().encode(
   	 x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
	st.dataframe(df.head())

	# Method 1 Using Write
	st.write(c)

	# Method 2 Using st.altair_chart
	st.altair_chart(c,use_container_width=True)





	

if __name__ == '__main__':
	main()










































