# api.py

from fastapi import FastAPI
from rag_pipeline import generate_answer

app = FastAPI(title="RAG API")


@app.get("/")
def home():
    return {"message": "RAG API Running"}


@app.get("/ask")
def ask(query: str):
    answer = generate_answer(query)
    return {"question": query, "answer": answer}
