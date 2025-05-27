import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

def get_api_key():
    try:
        return st.secrets["KEY"]
    except (KeyError, FileNotFoundError):
        return os.getenv("KEY")

def initialize_genai():
    api_key = get_api_key()
    
    if not api_key:
        st.error("❌ Google Gemini API key not found!")
        st.info("**For local development:** Add GOOGLE_GEMINI_API_KEY to your .env file")
        st.info("**For Streamlit Cloud:** Add GOOGLE_GEMINI_API_KEY to your app secrets")
        st.stop()
    
    genai.configure(api_key=api_key)
    return genai.GenerativeModel('gemini-1.5-flash')

def role_to_streamlit(role):
    if role == "model":
        return "assistant"
    else:
        return role

def initialize_session_state(model):
    if "chat" not in st.session_state:
        st.session_state.chat = model.start_chat(history=[])

def display_chat_history():
    for message in st.session_state.chat.history:
        with st.chat_message(role_to_streamlit(message.role)):
            st.markdown(message.parts[0].text)

def handle_user_input():
    """Handle user input and generate AI response."""
    if prompt := st.chat_input("I possess a well of knowledge. What would you like to know?"):
        # Display user message
        st.chat_message("user").markdown(prompt)
        
        try:
            # Send user entry to Gemini
            response = st.session_state.chat.send_message(prompt)
            
            # Display AI response
            with st.chat_message("assistant"):
                st.markdown(response.text)
                
        except Exception as e:
            st.error(f"Error generating response: {str(e)}")

def main():
    st.set_page_config(
        page_title="SachiChat",
        page_icon="💬",
        layout="centered",
        initial_sidebar_state="collapsed"
    )
    
    st.title("Hi! Welcome to SachiChat ✌")
    st.markdown("*Your AI-powered conversation companion*")
    
    model = initialize_genai()
    
    initialize_session_state(model)
    
    # Display chat history
    display_chat_history()
    
    # Handle user input
    handle_user_input()

if __name__ == "__main__":
    main()
