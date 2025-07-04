from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import requests
import os

# Set your GROQ API key here or use Streamlit secrets
GROQ_API_KEY = os.getenv("GROQ_API_KEY") or st.secrets.get("GROQ_API_KEY")

GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL_NAME = "llama3-70b-8192"

# App Title
st.title("📝 AI Story Generator")
st.write("Enter a story prompt and get a creative short story generated using LLaMA 3 via Groq API!")

# User Input
prompt = st.text_input("Enter your story prompt:", placeholder="E.g. A time traveler visits ancient Egypt")

# Generate button
if st.button("Generate Story") and prompt:
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "system", "content": "You are a creative storyteller who writes vivid, engaging short stories."},
            {"role": "user", "content": f"Write a short story based on this prompt: {prompt}"}
        ],
        "temperature": 0.8
    }

    with st.spinner("Generating your story..."):
        response = requests.post(GROQ_API_URL, headers=headers, json=data)
        if response.status_code == 200:
            story = response.json()["choices"][0]["message"]["content"]
            st.subheader("📖 Generated Story:")
            st.write(story)
        else:
            st.error("Failed to generate story. Please check your API key or try again later.")
