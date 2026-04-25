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


@st.cache_resource
def load_vectordb():
    data = scrape_page("https://bigomega.dev/blogs/learning-techniques")
    chunks = chunk_text(data["content"])
    embeddings = embed_chunks(chunks)
    db = VectorDB(dim=len(embeddings[0]))
    db.add(embeddings, chunks)
    return db


st.title("Local RAG Chatbot 🤖")

vectordb = load_vectordb()

query = st.text_input("Ask something:")

if query:
    answer = answer_query(query, vectordb)
    st.write(answer)