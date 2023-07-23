# Core Pkgs
import streamlit as st 

# Exercise Build a simple form
def main():
	st.title("Layout in Streamlit")
	st.subheader("Exercise: Build A Simple Form")
	
	# Firstname,Lastname,Age
	# Message,Contact

	col1,col2 = st.beta_columns(2)

	with col1:
		fname = st.text_input("Firstname")
		age = st.number_input("Age",1,100)
		message = st.text_area("Message")

	with col2:
		lname = st.text_input("Lastname")
		dob = st.date_input("Date of Birth")
		contact = st.text_input("Contact Address")


	template = f"Your name is {fname}, {lname} and you were born on {dob}. You said {message}"
	st.write(template)



	

if __name__ == '__main__':
	main()










































