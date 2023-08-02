import streamlit as st

st.title("User Registration")

with st.form("form1"):
    col1,col2 = st.columns(2)
    col1.text_input("First_Name")
    col2.text_input("Last_Name")
    st.text_input("Email")
    st.text_input("Password", type='password')
    st.text_input("Confirm Password",type='password')
    st.form_submit_button("Submit")


st.divider()
st.text("*******************************developed by Shyamu Sharma*******************************")    
