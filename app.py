import streamlit as st
from scraper import fetch_website_contents

st.set_page_config(
    page_title="Gemini Website Summarizer",
    page_icon="🌐",
    layout="centered"
)

st.title("🌐 Gemini Website Summarizer")

st.write(
    "Enter a website URL and let Gemini summarize its content."
)

url = st.text_input(
    "Website URL",
    placeholder="https://example.com"
)

summarize_button = st.button(
    "Summarize Website",
    type="primary"
)

if summarize_button:
    if url.strip():
        website_content = fetch_website_contents(url.strip())
        st.write(website_content)
    else:
        st.warning("Please enter a website URL.")