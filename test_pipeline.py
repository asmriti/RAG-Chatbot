from src.scraper import scrape_page
from src.chunker import chunk_text
from src.embedder import embed_chunks
from src.vectordb import VectorDB
from src.retriever import retrieve

data = scrape_page("https://bigomega.dev/blogs/learning-techniques")
chunks = chunk_text(data["content"])

embeddings = embed_chunks(chunks)

db = VectorDB(dim=len(embeddings[0]))
db.add(embeddings, chunks)

query = "What is this website about?"
results = retrieve(query, db)

print(results)