# Core Pkgs
import streamlit as st 
from PIL import Image


# Working with Multiple Files Upload
uploaded_file = st.file_uploader("Upload Files",type=["png","jpg"],
	accept_multiple_files=True)

# if uploaded_file is not None:
# 	img = Image.open(uploaded_file)
# 	st.image(img)

for file in uploaded_file:
	img = Image.open(file)
	st.image(img)








































