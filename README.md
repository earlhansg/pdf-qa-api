# 📚 AI-Powered PDF Knowledge Base API

Ask questions directly to your PDFs.  
This project provides a **Flask backend** that allows you to:

- Upload PDFs  
- Extract and embed text into a **vector database (Pinecone/Weaviate/Faiss)**  
- Query documents via a **REST or GraphQL API**  

---

## 🚀 Features

- 📄 **Upload PDFs** – research papers, reports, manuals, or any document  
- 🧩 **Text Extraction** – automatically parses PDF text  
- 🧠 **AI Embeddings** – generates vector representations of document chunks  
- 📦 **Vector Database** – stores embeddings in Pinecone / Weaviate / Faiss  
- 🔎 **Intelligent Search** – query documents in natural language (“Ask your PDF”)  
- 🌐 **API Ready** – REST + optional GraphQL endpoints for easy integration  
- 💻 **Frontend Friendly** – works with Next.js, React, or any frontend  

---

## 🛠 Tech Stack

- **Backend:** Flask (Python)  
- **Database:** Pinecone / Weaviate / Faiss  
- **AI Embeddings:** OpenAI / Hugging Face  
- **API:** REST + GraphQL (optional)  
- **Frontend (Demo):** Next.js  

---

## 📂 Project Structure

```bash
.
├── app.py              # Flask app entry point
├── routes/             # API routes (upload, query, etc.)
├── services/           # PDF parsing, embedding, DB handling
└── README.md           # Documentation
