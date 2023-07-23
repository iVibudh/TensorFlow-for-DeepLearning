# Core Pkgs
import streamlit as st 

# EDA Pkgs
import pandas as pd 
import numpy as np 

# Utils
import time

# Data Viz Pkgs
import matplotlib.pyplot as plt 
import matplotlib
matplotlib.use('Agg')
import seaborn as sns

def load_data(data):
	df = pd.read_csv(data)
	return df 


def main():
	st.title("Caching In Streamlit")

	start = time.time()
	df = load_data("iris.csv")
	end = time.time()
	st.text("Start:{}")

	st.dataframe(df)



if __name__ == '__main__':
	main()