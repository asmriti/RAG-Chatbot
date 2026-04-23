from src.embedder import model

def retrieve(query, vectordb, k=3):
    query_embedding = model.encode([query])[0]
    results = vectordb.search(query_embedding, k)
    return results