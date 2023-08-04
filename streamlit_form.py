import streamlit as st
import pandas as pd

st.title("User Registration")

with st.form("form1", clear_on_submit=True):
    col1,col2 = st.columns(2)
    f_name = col1.text_input("First_Name")
    l_name = col2.text_input("Last_Name")
    email = st.text_input("Email")
    pwd = st.text_input("Password", type='password')
    cpwd = st.text_input("Confirm Password",type='password')
    
    sub_state = st.form_submit_button("Submit")

    if sub_state:
        if f_name == "" and l_name == "" and email == "" and pwd =="" and cpwd =="":
            st.warning("Please fill above fields")
        else:
            st.success("Successfully Submitted !!")


st.divider()
st.text("*******************************developed by Shyamu Sharma*******************************")    

st.divider()

df = pd.DataFrame(
    [
       {"Company": "Google", "rating": 4, "is_mnc": True},
       {"Company": "Amazon", "rating": 5, "is_mnc": False},
       {"Company": "Meta", "rating": 3, "is_mnc": True},
       {"Company": "Microsoft", "rating": 3, "is_mnc": True},
       {"Company": "Pwc", "rating": 4, "is_mnc": True},
       {"Company": "ACC", "rating": 2, "is_mnc": False},
       {"Company": "Kyros", "rating": 1, "is_mnc": False},
   ]
)
edited_df = st.data_editor(df, num_rows="dynamic")

favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["Company"]
st.markdown(f"Your favorite Company is **{favorite_command}** 🎈")