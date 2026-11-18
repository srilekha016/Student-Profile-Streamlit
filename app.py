import streamlit as st
from groq import Groq
st.set_page_config(page_title = 'Student Profile' , layout='centered')
st.title("Student Profile Application")
st.caption("Developed by Student")
st.caption("Fill in your details and click View My Profile") 
name = st.text_input("Student Name",placeholder="Enter your name")
roll_no = st.text_input("USN Number",placeholder="Enter usn number")
department=st.selectbox("Department",['CSE', 'ISE', 'ECE', 'EEE', 'ME', 'Civil'])
year = st.radio("Current Year",['1st Year', '2nd Year', '3rd Year', '4th Year'])
if st.button("View My Profile"):
    if name and usn_no:
        st.success("Profile submitted successfully!")
        st.write("Name:", name)
        st.write("USN Number:", usn_no)
        st.write("Department:", department)
        st.write("Year:", year)
    else:
        st.warning("Please enter your name and roll number.")

