import openai

class GPTSummarizer:
    def __init__(self, api_key):
        openai.api_key = api_key

    def summarize(self, text, mode="section-wise"):
        prompt = f"""
You are an AI assistant summarizing scientific research papers.

Summarize the following text in a concise and structured way. Focus on important findings, methodology, and conclusions.
"""{text}"""
"""
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful research summarizer."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1000,
            temperature=0.5
        )
        return response.choices[0].message.content.strip()