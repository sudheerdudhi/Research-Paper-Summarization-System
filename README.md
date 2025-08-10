# Research Paper Summarization App

A Streamlit app that summarizes scientific research papers using Langchaing framework and Gemini API 2.5 flash.

## Features

- Upload PDF papers
- Automatic section detection (Abstract, Introduction, etc.)
- Section-wise summarization using GEMINI API KEY

## Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy to Streamlit Cloud

1. Push this folder to GitHub.
2. Go to https://google ai studio
3. Create a new app, link your repo, and set the `aistudio_API_KEY` in the secrets manager.
