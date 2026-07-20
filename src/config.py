import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    try:
        import streamlit as st
        API_KEY = st.secrets["GEMINI_API_KEY"]
    except Exception:
        API_KEY = None

if not API_KEY:
    raise ValueError(
        "GEMINI_API_KEY not found. Configure it in a local .env file or Streamlit Secrets."
    )

client = genai.Client(api_key=API_KEY)