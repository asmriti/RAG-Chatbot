import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

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

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "qwen3.5:latest",
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": 0.2,
                "num_predict": 300
            }
        }
    )

    return response.json()["response"]