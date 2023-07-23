# Core Pkgs
import streamlit as st 
from PIL import Image
img = Image.open("jcharistechlogo.png")
# Must be the first activity of streamlit
# st.beta_set_page_config(page_title='hello everyone') #Before 0.70.0


# Method 1
# st.set_page_config(page_title='hello',
# 	page_icon=img,layout='wide',
# 	initial_sidebar_state='auto') 


# Method 2:Dictionary
PAGE_CONFIG = {"page_title":"JCharisTech","page_icon":":smiley","layout":"centered"}
st.set_page_config(**PAGE_CONFIG)


# Additional Pkgs

# Fxns

def main():
	"""All your code goes here"""
	st.title("Hello Streamlit Lovers ❤️ 😃 😅")
	st.sidebar.success("Menu")



if __name__ == '__main__':
	main()
