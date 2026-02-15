# vector_store.py

from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings


PERSIST_DIRECTORY = "chroma_db"

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


def store_chunks(chunks):
    """
    Store chunks into Chroma vector DB with metadata.
    """

    texts = [chunk["content"] for chunk in chunks]
    metadatas = [
        {
            "source": chunk["source"],
            "doc_id": chunk["doc_id"]
        }
        for chunk in chunks
    ]

    vectordb = Chroma.from_texts(
        texts=texts,
        embedding=embedding_model,
        metadatas=metadatas,
        persist_directory=PERSIST_DIRECTORY
    )

    vectordb.persist()
    print("Chunks stored in vector database.")


def get_retriever():
    """
    Returns retriever for RAG pipeline.
    """

    vectordb = Chroma(
        persist_directory=PERSIST_DIRECTORY,
        embedding_function=embedding_model
    )

    return vectordb.as_retriever(search_kwargs={"k": 3})
