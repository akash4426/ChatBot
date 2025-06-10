import streamlit as st
from openai import OpenAI
import os


TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")


client = OpenAI(
    api_key=TOGETHER_API_KEY,
    base_url="https://api.together.xyz/v1"
)


if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful AI chatbot."}
    ]


st.title("🧠 Realangi mowayya (Ask anything)")


for msg in st.session_state.messages[1:]:  
    st.chat_message(msg["role"]).markdown(msg["content"])


user_input = st.chat_input("Type your message...")

if user_input:
    
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.chat_message("user").markdown(user_input)

    
    response = client.chat.completions.create(
        model="mistralai/Mistral-7B-Instruct-v0.1",
        messages=st.session_state.messages
    )

    
    reply = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.chat_message("assistant").markdown(reply)
