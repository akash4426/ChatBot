import streamlit as st
import openai
from dotenv import load_dotenv
import os
from googletrans import Translator

load_dotenv()
TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")


openai.api_key = TOGETHER_API_KEY
openai.api_base = "https://api.together.xyz/v1"


translator = Translator()


if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": (
                "You are a helpful assistant. Always reply in clear and simple Telugu language."
            )
        }
    ]


st.title("🥸🫂Relangi mowayya (తెలుగులో అడుగు)")


for msg in st.session_state.messages[1:]:
    st.chat_message(msg["role"]).markdown(msg["content"])


user_input = st.chat_input("మీ ప్రశ్నను టైప్ చేయండి...")

if user_input:
    
    translated_input = translator.translate(user_input, dest="en").text

    
    st.session_state.messages.append({"role": "user", "content": translated_input})
    st.chat_message("user").markdown(user_input)

    
    response = openai.ChatCompletion.create(
        model="meta-llama/Llama-3-8b-chat-hf",
        messages=st.session_state.messages
    )


    reply_raw = response.choices[0].message["content"].strip()
    reply_te = translator.translate(reply_raw, src="te",dest="te").text

    
    st.session_state.messages.append({"role": "assistant", "content": reply_raw})
    st.chat_message("assistant").markdown(reply_te)
