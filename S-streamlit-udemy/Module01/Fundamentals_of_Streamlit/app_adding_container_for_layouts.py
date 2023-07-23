# Core Pkgs
import streamlit as st 


def main():
	st.title("Multi Element Container in Streamlit")
	st.text("Multiple elements out of order ")

	# Method 1
	# container = st.beta_container()
	# st.success("Hello")
	# container.info("This is from container")

	# Method 2: Context Manager
	with st.beta_container():
		st.success("From Inside Container 1")
		st.write("From Inside Container")


	st.warning("From Outside Container")

	



	

if __name__ == '__main__':
	main()










































