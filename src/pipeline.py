from src.retriever import retrieve
from src.llm import generate_answer

def answer_query(query, vectordb):
    chunks = retrieve(query, vectordb)
    context = "\n\n".join(chunks)

    return generate_answer(query, context)