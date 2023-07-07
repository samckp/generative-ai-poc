# python-streamlit-poc
<h3>Tech : PandasAI, OpenAI and Streamlit - Analyze Uploaded CSV File with User Prompts</h3>
<hr>
Requirement : 
1. pip install PandasAI
2. pip install OpenAI
3. pip install Streamlit

Streamlit to build a small UI that allows users to upload a file of CSV data, and will create a text input and buttons that allow users to submit a prompt that can then be used to analyze and interrogate the data.


The prompt will be passed to the PandasAI library, which will take care of sending that prompt along with the data to OpenAI for analysis via their LLMs.

<h3>How to run application </h3>
<hr>
project folder > streamlit run read_csv_analyse.py <press enter> 
open a browser with http://localhost:8501/
