import streamlit as st
from groq import Groq
st.set_page_config(page_title = 'Student Profile' , layout='centered')
st.title("Student Profile Application")
st.caption("Developed by Student")
st.caption("Fill in your details and click View My Profile") 
name = st.text_input("Student Name",placeholder="Enter your name")
roll_no = st.text_input("USN/Roll Number",placeholder="Enter roll number")

