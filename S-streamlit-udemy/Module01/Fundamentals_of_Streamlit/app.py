# Core Pkgs
import streamlit as st 

# Load EDA Pkgs
import pandas as pd 
import numpy as np



def main():
	st.title("Plotting In Streamlit")
	# Load Dataset
	# df = pd.read_csv("data/iris.csv")
	df = pd.read_csv("data/lang_data.csv")
	st.dataframe(df.head())

	# Plotting with Plotly

	

	

if __name__ == '__main__':
	main()










































