import streamlit as st


def changed():
    print("Changed !")

state = st.checkbox("checkbox", value=True, on_change=changed)

print(state)

rd = st.radio("Country ?", options=("US", "UK","SL","IND"))
print(rd)                                  

def click():
    print("Submitted")
btn = st.button("Submit" , on_click=click)

select = st.selectbox("Cars", options=("Audi", "Merc","Tata", "Kia", "Toyota"))
print(select)

multi_select = st.multiselect("Favourite Language", options=("French", "Dutch", "Eng", "Hindi","Spanish"))