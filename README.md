Retrieval-Augmented Generation (RAG) System

AI Intern Assessment Submission

Project Overview

This project implements a Retrieval-Augmented Generation (RAG) system as part of the AI Intern assessment. The system scrapes content from a real-world website, validates the scraped data using a defined JSON schema, chunks the content, stores embeddings in a vector database, and retrieves relevant information to generate answers using a language model.

The goal of this project is to build a complete end-to-end RAG pipeline that demonstrates proper system design, data validation, retrieval logic, and controlled answer generation.

Data Source

For demonstration, the system scrapes data from:

https://en.wikipedia.org/wiki/Artificial_intelligence

The architecture is modular and can be extended to work with other websites by modifying the input URL.

Data Scraping

The website content is scraped using requests and BeautifulSoup.

During scraping:

Script and style elements are removed.

Only paragraph text is extracted.

Very short or duplicate content is filtered out.

Each scraped record contains:

id (unique identifier)

source (website URL)

content (paragraph text)

length (character count)

JSON Validation

The scraped data is validated using a Pydantic schema before further processing.

Validation ensures:

Required fields are present.

Content is not empty.

Content meets minimum length requirements.

Invalid records are excluded from further processing. This prevents malformed data from entering the vector store and ensures robustness of the pipeline.

Chunking Strategy

The validated text is chunked using a recursive character text splitter.

Configuration used:

Chunk size: 500

Chunk overlap: 100

Reasoning:
Smaller chunks improve retrieval precision because embeddings represent more focused semantic content. Overlap is used to prevent context loss between chunk boundaries. The selected values balance contextual completeness and retrieval accuracy.

Embedding Model

Embeddings are generated using:

sentence-transformers/all-MiniLM-L6-v2

This model was chosen because:

It is lightweight.

It generates efficient 384-dimensional embeddings.

It provides good semantic similarity performance.

It works well for local inference.

Vector Store

ChromaDB is used as the vector database.

Reasons for choosing Chroma:

Easy local setup.

Persistent storage.

Efficient similarity search.

No external infrastructure required.

The embeddings and metadata are stored in a persistent directory for retrieval.

Retrieval Process

When a user asks a question:

The question is embedded.

Top-k similar chunks are retrieved using cosine similarity.

The retrieved context is passed to the language model.

The model generates a grounded answer using only the retrieved context.

Top-k retrieval improves relevance while maintaining response efficiency.

Language Model Integration

A HuggingFace model is used for answer generation.

The prompt is designed to:

Restrict the model to use only the retrieved context.

Avoid hallucination.

Provide clear and concise answers.

Indicate when information is not available in the knowledge base.

How to Run the Project

Clone the repository:

git clone <repository_url>

Create a virtual environment:

python -m venv venv
venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Run the full pipeline:

python main.py

Run Streamlit UI:

streamlit run app.py

Run API (optional):

uvicorn api:app --reload

Project Structure

web_scraper.py – Scrapes website data

schema.py – Validates JSON data

chunking.py – Implements chunking strategy

vector_store.py – Stores and retrieves embeddings

rag_pipeline.py – Implements RAG logic

main.py – Runs full pipeline

app.py – Streamlit interface

api.py – FastAPI endpoint

system_prompt.txt – Prompt template

requirements.txt – Dependencies

Conclusion

This project demonstrates a complete Retrieval-Augmented Generation system including scraping, validation, chunking, vector storage, retrieval, and answer generation. The implementation focuses on modular design, clean data handling, and controlled generation to ensure reliable and explainable responses.