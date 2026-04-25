import os

import google.generativeai as genai

def _api_key() -> str:
    key = os.getenv("GEMINI_API_KEY")
    if not key:
        raise RuntimeError(
            "GEMINI_API_KEY is not set. Export it in your shell, or define it in your "
            "environment before starting the app (e.g. `export GEMINI_API_KEY=...`)."
        )
    return key


genai.configure(api_key=_api_key())
_MODEL = genai.GenerativeModel("gemini-2.5-flash")

def generate_answer(query, context):
    prompt = f"""
### Instructions:
- Answer ONLY using the provided context
- Do NOT make up information
- If unsure, say "I don't know"

### Context:
{context}

### Question:
{query}

### Answer:
"""
    response = _MODEL.generate_content(
        prompt,
        generation_config={
            "temperature": 0.2,
            "max_output_tokens": 300,
        },
    )

    return response.text
