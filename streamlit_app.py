import streamlit as st
from langchain.llms import OpenAI


st.header('Text Submit Chatbox App', divider = 'rainbow')

openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')

def generate_response(input_text):
    llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
    st.info(llm(input_text))

with st.form('my_form'):
    text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
    submitted = st.form_submit_button('Submit')
    if not openai_api_key.startswith('sk-'):
        st.warning('Please enter your OpenAI API key!', icon='⚠')
    if submitted and openai_api_key.startswith('sk-'):
        generate_response(text)
		

st.header('Frosty LLM Chatbox', divider = 'rainbow')

conn = st.experimental_connection(**st.secrets["snowflake"])
df = conn.query("select current_warehouse()")
df