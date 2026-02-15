from transformers import pipeline
from vector_store import get_retriever

# Use a causal model (simplest & stable)
hf_pipeline = pipeline(
    "text-generation",
    model="distilgpt2",
    max_new_tokens=150,
    temperature=0.3,
    pad_token_id=50256
)


retriever = get_retriever()


def generate_answer(question: str) -> str:
    """
    Custom RAG pipeline implementation.
    """

    # Step 1: Retrieve relevant documents
    docs = retriever.get_relevant_documents(question)

    context = "\n\n".join([doc.page_content for doc in docs])

    # Step 2: Create clean prompt
    prompt = f"""
Answer the question using ONLY the context below.
If the answer is not present, say:
"The information is not available in the knowledge base."

Context:
{context}

Question:
{question}

Answer:
"""

    # Step 3: Generate answer
    result = hf_pipeline(prompt)[0]["generated_text"]

    return result.strip()






# from langchain.llms import HuggingFacePipeline
# from langchain.chains import RetrievalQA
# from langchain.prompts import PromptTemplate
# from transformers import pipeline
# from vector_store import get_retriever


# # Load system prompt
# with open("system_prompt.txt", "r") as f:
#     system_prompt = f.read()


# # Initialize local HuggingFace model
# hf_pipeline = pipeline(
#     "text-generation",
#     model="google/flan-t5-base",
#     max_new_tokens=256
# )

# llm = HuggingFacePipeline(pipeline=hf_pipeline)


# # Custom Prompt Template
# PROMPT = PromptTemplate(
#     template=system_prompt,
#     input_variables=["context", "question"]
# )


# retriever = get_retriever()

# qa = RetrievalQA.from_chain_type(
#     llm=llm,
#     retriever=retriever,
#     chain_type="stuff",
#     chain_type_kwargs={"prompt": PROMPT}
# )


# def generate_answer(question: str) -> str:
#     return qa.run(question)
