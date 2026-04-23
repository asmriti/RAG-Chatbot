from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_chunks(chunks):
    return model.encode(chunks)

if __name__ == "__main__":
    chunks = ["Hello, how are you?", "I am fine, thank you."]
    embeddings = embed_chunks(chunks)
    print(embeddings)