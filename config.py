import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

class Config:
    @staticmethod
    def get_api_key():
        try:
            return st.secrets["KEY"]
        except (KeyError, FileNotFoundError):
            return os.getenv("KEY")

    KEY = get_api_key()
    PAGE_TITLE = "SachiChat"
    PAGE_ICON = "💬"
    
    MODEL_NAME = "gemini-1.5-flash"
    DEFAULT_PLACEHOLDER = "I possess a well of knowledge. What would you like to know?"
    WELCOME_MESSAGE = "Hi! Welcome to SachiChat ✌"
    
    @classmethod
    def validate_config(cls):
        if not cls.KEY:
            st.error("❌ Google Gemini API key not found!")
            st.info("For local development: Add GOOGLE_GEMINI_API_KEY to your .env file")
            st.info("For Streamlit Cloud: Add GOOGLE_GEMINI_API_KEY to your app secrets")
            st.stop()
        return True
