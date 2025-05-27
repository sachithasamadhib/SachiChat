import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

def initialize_genai():
    api_key = os.getenv("KEY")
    
    if not api_key:
        st.error("Google Gemini API key not found. Please check your .env file.")
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
    if prompt := st.chat_input("What would you like to know?"):
        st.chat_message("user").markdown(prompt)
        
        try:
            response = st.session_state.chat.send_message(prompt)
            
            with st.chat_message("assistant"):
                st.markdown(response.text)
                
        except Exception as e:
            st.error(f"Error generating response: {str(e)}")
            try:
                models = genai.list_models()
                st.write("Available models:")
                for model in models:
                    if 'generateContent' in model.supported_generation_methods:
                        st.write(f"- {model.name}")
            except:
                pass

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
    display_chat_history()

    handle_user_input()

if __name__ == "__main__":
    main()