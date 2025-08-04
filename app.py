import streamlit as st
import google.generativeai as genai
import os

# Get API key from environment variables
api_key = os.environ.get("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

if not api_key:
    st.error("API Key not found. Please set the GOOGLE_API_KEY environment variable.")
