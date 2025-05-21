import streamlit as st
from summarizer import GPTSummarizer
from utils import extract_text_from_pdf, split_into_sections
import os
from dotenv import load_dotenv

load_dotenv()
st.set_page_config(page_title="Research Paper Summarizer", layout="wide")

st.title("📄 Research Paper Summarizer")
st.write("Upload a research paper PDF to generate a summary using GPT + SciBERT.")

api_key = os.getenv("OPENAI_API_KEY") or st.text_input("🔑 Enter OpenAI API Key", type="password")

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file and api_key:
    with st.spinner("Extracting text from PDF..."):
        with open("temp.pdf", "wb") as f:
            f.write(uploaded_file.read())
        raw_text = extract_text_from_pdf("temp.pdf")

    sections = split_into_sections(raw_text)

    st.subheader("📚 Detected Sections")
    for section, content in sections.items():
        st.markdown(f"### {section.capitalize()}")
        st.text(content[:500] + "..." if len(content) > 500 else content)

    if st.button("🔍 Summarize Sections"):
        summarizer = GPTSummarizer(api_key)
        with st.spinner("Generating section-wise summary..."):
            full_summary = ""
            for section, content in sections.items():
                section_summary = summarizer.summarize(content[:2000], mode="brief")
                full_summary += f"### {section.capitalize()}
{section_summary}

"
        st.subheader("📌 Section-wise Summary")
        st.markdown(full_summary)
else:
    st.info("Please upload a PDF and enter your OpenAI API key.")