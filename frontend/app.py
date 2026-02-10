import streamlit as st
import requests

st.set_page_config(page_title="RAG Assistant", page_icon="📄")
st.title("📄 Document Chat Assistant")

# Upload PDF
uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file:
    with st.spinner("Processing document..."):
        res = requests.post(
            "http://127.0.0.1:8000/upload",
            files={"file": uploaded_file.getvalue()}
        )
    st.success("Document ready! Ask questions below.")

# Chat
question = st.text_input("Ask a question about the document")

if st.button("Ask"):
    res = requests.get(
        "http://127.0.0.1:8000/ask",
        params={"question": question}
    )
    st.write(res.json()["answer"])
