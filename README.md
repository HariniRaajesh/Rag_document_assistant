# 📄 Document Chat Assistant (RAG)

An end-to-end Retrieval Augmented Generation (RAG) system that allows users to upload PDF documents and ask natural language questions about them.

The system retrieves relevant document chunks using vector similarity search and returns grounded answers with sources.

---

## 🚀 Features

* Upload PDF documents
* Semantic search using embeddings
* Context-aware question answering
* Source page citation
* Interactive chat UI

---

## 🧠 Tech Stack

* Python
* FastAPI
* Streamlit
* LangChain
* HuggingFace Embeddings
* FAISS Vector Database

---

## 🏗️ Architecture

User → Upload PDF → Chunking → Embeddings → FAISS
User Question → Retriever → Context → Answer

---

## ▶️ How to Run

### 1. Clone repo

```bash
git clone https://github.com/yourusername/rag-document-assistant.git
cd rag-document-assistant
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run backend

```bash
python -m uvicorn backend.main:app --reload
```

### 4. Run frontend

```bash
streamlit run frontend/app.py
```

---

## 📷 Demo

Upload a PDF and ask:

> “What is the main topic of the document?”

The assistant retrieves relevant sections and answers with sources.

---

## 🎯 Use Cases

* Enterprise document search
* Resume screening
* Legal document analysis
* Knowledge base assistants
## Demo

### Upload
![Upload](screenshots/upload.png)

### Question
![Question](screenshots/question.png)

### Answer
![Answer](screenshots/answer.png)

