# Core Pkgs
import streamlit as st 
import docx2txt
import pdfplumber
import pandas as pd 


# Working with File Upload
uploaded_file = st.file_uploader("Upload Files",type=["txt","pdf","docx","csv"])
file_type = st.selectbox("Select File Type",["txt","pdf","docx","csv"])
if st.button("Submit"):
	# Reading TXT
	if uploaded_file is not None:
		if file_type == 'txt':
			processed_file = uploaded_file.read().decode('utf-8')
		elif file_type == 'docx':
			processed_file = docx2txt.process(uploaded_file)
		elif file_type == 'pdf':
			with pdfplumber.open(uploaded_file) as pdf_file:
				pages = pdf_file.pages[0]
				processed_file = pages.extract_text()
		elif file_type == 'csv':
			processed_file = pd.read_csv(uploaded_file)
			



		
		st.write(processed_file)







































