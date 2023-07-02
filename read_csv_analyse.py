import streamlit as st
import pandas as pd
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI

# create an LLM by instantiating OpenAI object, and passing API token
llm = OpenAI(api_token="sk-")

pandas_ai = PandasAI(llm)

st.title("Prompt-driven data analysis with PandasAI")
uploaded_file = st.file_uploader("Upload a CSV file for analysis", type=['csv'])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Date Preview")
    st.write(df.head(10))

    prompt = st.text_area("Enter your prompt:")

    # Generate output
    if st.button("Generate"):
        if prompt:            
            with st.spinner("Generating response..."):
                st.write(pandas_ai.run(df, prompt))
        else:
            st.warning("Please enter a prompt.")





