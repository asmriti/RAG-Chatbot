from pathlib import Path
import sys

import streamlit as st

# Ensure imports from the project root work when running from `app/`.
PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.chunker import chunk_text
from src.embedder import embed_chunks
from src.pipeline import answer_query
from src.scraper import scrape_page
from src.vectordb import VectorDB


def _normalize_url(url: str) -> str:
    url = url.strip()
    if not url:
        return ""
    if not url.startswith(("http://", "https://")):
        return f"https://{url}"
    return url


@st.cache_resource
def load_vectordb(url: str):
    data = scrape_page(url)
    chunks = chunk_text(data["content"])
    if not chunks:
        raise ValueError(
            "No paragraph text was found on this page. Try another URL or a page with readable body text."
        )
    embeddings = embed_chunks(chunks)
    db = VectorDB(dim=len(embeddings[0]))
    db.add(embeddings, chunks)
    return db


st.title("Local RAG Chatbot 🤖")

url_raw = st.text_input(
    "Paste a website URL here:",
    value="",
    help="The chatbot answers using text scraped from this page (paragraphs only).",
)
url = _normalize_url(url_raw)

query = st.text_input("Ask something about this page:")

if query:
    if not url:
        st.warning("Paste the URL above first, then ask your question.")
        st.stop()

    try:
        vectordb = load_vectordb(url)
    except Exception as e:
        st.error(f"Could not load this URL: {e}")
        st.stop()

    answer = answer_query(query, vectordb)
    st.write(answer)
