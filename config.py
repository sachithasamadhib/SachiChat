import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    GOOGLE_GEMINI_API_KEY = os.getenv("KEY")
    
    PAGE_TITLE = "SachiChat"
    PAGE_ICON = "💬"
    MODEL_NAME = "gemini-1.5-flash"
    DEFAULT_PLACEHOLDER = "What would you like to know?"
    WELCOME_MESSAGE = "Hi! Welcome to SachiChat ✌"
    
    @classmethod
    def validate_config(cls):
        if not cls.GOOGLE_GEMINI_API_KEY:
            raise ValueError("GOOGLE_GEMINI_API_KEY environment variable is required")
        return True
