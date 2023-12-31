import streamlit as st
import time
from response_logic import get_gita_response

def interface():
    st.title("Gita Chatbot")

    # Set a default model
    if "llama_model" not in st.session_state:
        st.session_state["llama_model"] = "llama-2-7b-hf"

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Accept user input
    if prompt := st.chat_input("Ask any question you wish to seek spiritual guidance on: "):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)
        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            # Response logic
            assistant_response = get_gita_response(prompt)
        if assistant_response is None:
            assistant_response = "Sorry, I don't understand that. Please try again."
        # Simulate stream of response with milliseconds delay
        for chunk in assistant_response.split():
            full_response += chunk + " "
            time.sleep(0.05)
            # Add a blinking cursor to simulate typing
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": full_response})


# start the app
interface()