import streamlit as st

st.markdown("<h1>User Registration </h1>")

with st.form("form1"):
    col1,col2 = st.columns(2)
    col1.text_input("First_Name")
    col2.text_input("Last_Name")
    st.text_input("Email")
    st.text_input("Password")
    st.text_input("Confirm Password")
    st.form_submit_button("Submit")

