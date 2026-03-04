import streamlit as st
from llama_index.core.llms import ChatMessage
import logging
import time
from llama_index.llms.ollama  import Ollama
import requests


if 'messages' not in st.session_state:
    st.session_state.messages = []

# Function to stream chat response based on selected model
def stream_chat(model, messages):
    #Tries to stream the model
    try:
        llm = Ollama(model=model, request_timeout=120.0) 
        resp = llm.stream_chat(messages)
        response = ""
        response_placeholder = st.empty()
        for r in resp:
            response += r.delta
            response_placeholder.write(response)
        logging.info(f"Model: {model}, Messages: {messages}, Response: {response}")
        return response
    # Log and re-raise any errors that occur
    except Exception as e:
        logging.error(f"Error during streaming: {str(e)}")
        raise e
    
# Get ollama names
def get_ollama_model_names(host='http://localhost:11434'):
    try:
        response = requests.get(f"http://localhost:11434/api/tags")
        if response.status_code == 200:
            models = response.json().get('models', [])
            return [model['name'] for model in models]
        else:
            print(f"Error: Server returned status {response.status_code}")
            return []
    except requests.exceptions.RequestException as e:
        print(f"Connection error: {e}")
        return []
