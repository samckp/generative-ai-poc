import streamlit as st
import pandas as pd

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