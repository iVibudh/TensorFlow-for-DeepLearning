# Core Pkgs
import streamlit as st 

# Load EDA Pkgs
import pandas as pd 
import numpy as np

# Load Data Viz Pkgs
import matplotlib.pyplot as plt 
import matplotlib
matplotlib.use('Agg') # TkAgg
import seaborn as sns


def main():
	st.title("Plotting with St.Pyplot")
	df = pd.read_csv("data/iris.csv")

	st.dataframe(df.head())

	# Previous Method
	# df['species'].value_counts().plot(kind='bar')
	# st.pyplot()

	# plt.scatter(*np.random.random(size=(2,100)))
	# st.pyplot()

	# Recommended Method
	fig,ax = plt.subplots()
	ax.scatter(*np.random.random(size=(2,100)))
	st.pyplot(fig)

	# Method 2: Simple Method
	fig = plt.figure()
	df['species'].value_counts().plot(kind='bar')
	st.pyplot(fig)

	# Method 3
	# fig,ax = plt.subplots()
	# df['species'].value_counts().plot(kind='bar')
	# st.pyplot(fig)


	# Alternative For Matplotlib
	fig = plt.figure()
	sns.countplot(df['species'])
	st.pyplot(fig)












	
	



	

if __name__ == '__main__':
	main()










































