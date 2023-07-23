# Core Pkgs
import streamlit as st 

# Text Input
fname = st.text_input("Enter Firstname")
# Text Input Hide Password
password = st.text_input("Enter Password",type='password')
st.title(fname)

# Text Area
message = st.text_area("Enter Message",height=100)
st.write(message)

# Numbers
number = st.number_input("Enter Number",1.0,25.0)

# Date Input
myappointment = st.date_input("Appointment")

# Time Input
mytime = st.time_input("My Time")


# Color Picker
color = st.beta_color_picker("Select Color")





































