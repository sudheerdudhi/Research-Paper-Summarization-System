# Research Paper Summarization App

A Streamlit app that summarizes scientific research papers using SciBERT + GPT-4.

## Features

- Upload PDF papers
- Automatic section detection (Abstract, Introduction, etc.)
- Section-wise summarization using GPT-4

## Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy to Streamlit Cloud

1. Push this folder to GitHub.
2. Go to https://streamlit.io/cloud
3. Create a new app, link your repo, and set the `OPENAI_API_KEY` in the secrets manager.