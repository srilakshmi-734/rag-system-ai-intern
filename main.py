# main.py

from web_scraper import scrape_website, save_to_json
from schema import validate_data
from chunking import chunk_documents
from vector_store import store_chunks
from rag_pipeline import generate_answer


def main():

    url = "https://en.wikipedia.org/wiki/Artificial_intelligence"

    print("\nStep 1 — Scraping")
    raw_data = scrape_website(url)
    save_to_json(raw_data)

    print("\nStep 2 — Validation")
    valid_data, errors = validate_data(raw_data)

    print(f"Valid records: {len(valid_data)}")
    print(f"Validation errors: {len(errors)}")

    print("\nStep 3 — Chunking")
    chunks = chunk_documents(valid_data)
    print(f"Total chunks created: {len(chunks)}")

    print("\nStep 4 — Storing in Vector DB")
    store_chunks(chunks)

    print("\nStep 5 — Asking Question")
    question = "What is artificial intelligence?"
    answer = generate_answer(question)

    print("\nFinal Answer:\n")
    print(answer)


if __name__ == "__main__":
    main()
