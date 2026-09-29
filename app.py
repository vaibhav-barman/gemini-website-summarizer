import streamlit as st

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
        st.info(f"URL entered: {url.strip()}")
    else:
        st.warning("Please enter a website URL.")