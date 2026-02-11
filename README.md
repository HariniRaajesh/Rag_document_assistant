🧠 Document Chat Assistant (RAG)
  Ask questions from any PDF — get accurate answers from the document itself.
🔗 Live App: http://16.170.158.230
📑 API Docs: http://16.170.158.230/docs

✨ What this project does
Upload a PDF → Ask a question → System finds the most relevant parts → Returns a grounded answer.
No hallucinations. Only document-based responses.

⚙️ How it works
PDF → Text → Chunks → Embeddings → FAISS Index
                                   ↑Question → Embedding → Similarity Search → Context → Answer
                                   
🏗️ Tech Stack
 Backend
  * FastAPI
  * LangChain
  * Sentence-Transformers (MiniLM)
  * FAISS Vector Store
    
Frontend
  * Streamlit
    
Deployment
  * AWS EC2 (Ubuntu)
  * Nginx reverse proxy
  * Background services (tmux)

🚀 Features
  * Upload any PDF
  * Semantic document search
  * Context-aware answers
  * Interactive UI
  * Live deployed API
    
▶️ Run locally
git clone https://github.com/HariniRaajesh/Rag_document_assistant.git
cd Rag_document_assistant
pip install -r requirements.txt
uvicorn backend.main:app --reload
streamlit run frontend/app.py

💡 Use cases
  * Knowledge base assistants
  * Research paper Q&A
  * Legal document analysis
  * Resume screening tools

👩‍💻 Author
  Harini
## Demo

### Upload
![Upload](screenshots/Upload.png)

### Question
![Question](screenshots/Question.png)

### Answer
![Answer](screenshots/Answer.png)




