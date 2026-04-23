import faiss
import numpy as np

class VectorDB:
    def __init__(self, dim):
        self.index = faiss.IndexFlatL2(dim)
        self.texts = []

    def add(self, embeddings, texts):
        self.index.add(np.array(embeddings))
        self.texts.extend(texts)

    def search(self, query_embedding, k=3):
        distances, indices = self.index.search(
            np.array([query_embedding]), k
        )
        return [self.texts[i] for i in indices[0]]

if __name__ == "__main__":
    vectordb = VectorDB(dim=128)
    embeddings = [[0.1, 0.2, 0.3], [0.4, 0.5, 0.6], [0.7, 0.8, 0.9]]
    texts = ["text1", "text2", "text3"]
    vectordb.add(embeddings, texts)
    query_embedding = [0.1, 0.2, 0.3]
    print(vectordb.search(query_embedding))