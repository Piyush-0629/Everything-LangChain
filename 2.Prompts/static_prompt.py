from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate,load_prompt

load_dotenv()
model = ChatOpenAI(model="gpt-4o-mini", temperature = 0)

st.header('Reasearch Tool')

user_input = st.text_input('Enter your question')

if st.button('Summarize'):
    result = model.invoke(user_input)
    st.write(result.content)