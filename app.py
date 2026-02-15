import streamlit as st
from rag_pipeline import generate_answer

# Page config
st.set_page_config(
    page_title="AI RAG Chatbot",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI RAG Chatbot")
st.write("Ask questions based on scraped website data.")



# Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])



# User Input
user_input = st.chat_input("Ask a question...")

if user_input:

    # Show user message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate answer
    with st.spinner("Thinking..."):
        try:
            answer = generate_answer(user_input)

            if not answer or answer.strip() == "":
                answer = "⚠️ No relevant information found."

        except Exception as e:
            answer = f"Error: {str(e)}"

    # Show assistant message
    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )

    with st.chat_message("assistant"):
        st.markdown(answer) 
