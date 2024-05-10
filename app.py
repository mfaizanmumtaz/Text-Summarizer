prompt_template = """Write a concise summary of the following:
"{text}"
CONCISE SUMMARY:"""

from langchain.schema.output_parser import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
import os

prompt = PromptTemplate.from_template(prompt_template)

llm = ChatGoogleGenerativeAI(temperature=0, model="gemini-pro",google_api_key=os.getenv("GOOGLE_API_KEY"))
chain = prompt | llm | StrOutputParser()

import streamlit as st
st.set_page_config(page_icon=":pencil2:", page_title="Text Summarizer")
st.title("Text Summarizer 📝")

text = st.text_area("Enter text")
if st.button("Generate Summary"):
    with st.spinner("Generating summary..."):
        response = chain.invoke(
                {"text": text})
        st.chat_message("assistant").write(response)