# RAG Chatbot (URL-Based)

A simple Retrieval-Augmented Generation (RAG) chatbot built with Streamlit.

The app:
- takes a website URL from user input
- scrapes paragraph text from that page
- chunks and embeds the content
- stores embeddings in FAISS
- answers questions using Gemini based only on retrieved context

## Tech Stack

- Python 3.11+
- Streamlit
- SentenceTransformers (`all-MiniLM-L6-v2`) for embeddings
- FAISS for vector search
- Google Gemini (`google-generativeai`) for answer generation
- `uv` for dependency management and running

## Prerequisites

- Python 3.11 or newer
- `uv` installed
- A Gemini API key

Install `uv` if needed:

```bash
pip install uv
```

## Setup

From the project root:

```bash
uv sync
```

Set your API key:

```bash
export GEMINI_API_KEY="your_api_key_here"
```

> Do not hardcode keys in source files. Keep keys in environment variables or secret managers.

## Run the App

```bash
uv run streamlit run app/main.py
```

Streamlit will print a local URL (usually `http://localhost:8501`).

## How to Use

1. Paste a website URL in **"Paste a website URL here:"**
2. Ask a question in **"Ask something about this page:"**
3. The chatbot answers based on content scraped from that specific URL

If you ask a question without entering a URL first, the app shows a warning.

## Notes and Limitations

- The scraper currently extracts only `<p>` paragraph text.
- Some modern websites render content with JavaScript; those pages may return little or no content.
- Responses are instructed to stay within retrieved context, but quality depends on page content and retrieval.

## Project Structure

```text
app/
  main.py          # Streamlit UI
src/
  scraper.py       # Website scraping
  chunker.py       # Text chunking
  embedder.py      # Embedding generation
  vectordb.py      # FAISS wrapper
  retriever.py     # Top-k retrieval
  llm.py           # Gemini answer generation
  pipeline.py      # Query -> retrieve -> generate flow
```
