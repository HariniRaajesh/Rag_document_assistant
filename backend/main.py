from fastapi import FastAPI, UploadFile
from backend.rag import build_vectorstore, get_answer
import shutil
import os

app = FastAPI()

vectorstore = None


@app.post("/upload")
def upload_pdf(file: UploadFile):
    global vectorstore

    os.makedirs("data/pdfs", exist_ok=True)
    path = f"data/pdfs/{file.filename}"

    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    vectorstore = build_vectorstore(path)
    return {"message": "PDF processed successfully"}


@app.get("/ask")
def ask(question: str):
    if vectorstore is None:
        return {"error": "Upload PDF first"}

    answer = get_answer(vectorstore, question)
    return {"answer": answer}
