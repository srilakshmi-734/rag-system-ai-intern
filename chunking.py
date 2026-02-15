# chunking.py

from langchain.text_splitter import RecursiveCharacterTextSplitter


def chunk_documents(documents):
    """
    Chunk documents using recursive semantic splitter.
    """

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    all_chunks = []

    for doc in documents:
        chunks = text_splitter.split_text(doc["content"])

        for chunk in chunks:
            all_chunks.append({
                "content": chunk,
                "source": doc["source"],
                "doc_id": doc["id"]
            })

    return all_chunks
