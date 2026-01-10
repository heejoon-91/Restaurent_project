from openai import OpenAI
import streamlit as st

def get_openai_client():
    return OpenAI(
        api_key=st.secrets["OPENAI_API_KEY"]
    )