# Core Pkgs
import streamlit as st 


def main():
	st.title("Layout in Streamlit")

	# Former Layout
	st.success("Full Length Wide Layout")

	# Layout/Gridlike COlumns
	col1,col2 = st.beta_columns(2)
	# Method 1
	# st.write(dir(col1))
	col1.success("Col1")
	col2.warning("Col2")

	# Method 2: Context Manager with
	with col1:
		st.info("From Col1")
		fname = st.text_input("Firstname")

	with col2:
		st.success("From col2")

	# # 3 Columns
	# c1,c2,c3 = st.beta_columns(3)

	# with c1:
	# 	st.success("From C1")

	# with c2:
	# 	st.success("From C2")

	# with c3:
	# 	st.info("From C3")


	# Unequal width
	c1,c2 = st.beta_columns([3,1])
	with c1:
		st.success("From C1 3x larger")

	with c2:
		st.info("From C2: less")





















if __name__ == '__main__':
	main()










































