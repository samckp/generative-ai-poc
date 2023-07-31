import streamlit as st
from PIL import Image

def changed():
    print("Changed !")

state = st.checkbox("checkbox", value=True, on_change=changed)

print(state)

rd = st.radio("Country ?", options=("US", "UK","SL","IND"))
print(rd)                                  

def click():
    print("Submitted")
btn = st.button("Submit" , on_click=click)

# select box / combo box
select = st.selectbox("Cars", options=("Audi", "Merc","Tata", "Kia", "Toyota"))
print(select)

#Multiselect box
multi_select = st.multiselect("Favourite Language", options=("French", "Dutch", "Eng", "Hindi","Spanish"))

## file uploader
 
images = st.file_uploader("Upload images", type=['png', 'jpg'])
image = Image.open(images)
st.image(image)

           