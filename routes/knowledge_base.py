import os
from flask import Blueprint, request, jsonify
from pinecone import Pinecone
from sentence_transformers import SentenceTransformer
import PyPDF2
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env

knowledge_base_bp = Blueprint("knowledge_base_bp", __name__)

# Load Local embeddings Model
embed_model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
EMBED_DIM = embed_model.get_sentence_embedding_dimension()

# Pinecone client
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

INDEX_NAME = "test-index"

if not pc.has_index(INDEX_NAME):
    pc.create_index(
        name=INDEX_NAME,
        dimension=EMBED_DIM,
        metric="cosine",
        spec={"serverless": {"cloud": "aws", "region": "us-east-1"}}
    )


index = pc.Index(INDEX_NAME)

# Chunking
def chunk_text(text, max_tokens=300, overlap=50):
    words = text.split()
    chunks = []
    i = 0
    while i < len(words):
        chunk = words[i:i+max_tokens]
        chunks.append(" ".join(chunk))
        i += max_tokens - overlap
    return chunks

@knowledge_base_bp.route("/upload", methods=["POST"])
def upload_pdf():
    file = request.files["file"]
    pdf_reader = PyPDF2.PdfReader(file)

    all_chunks = []
    ids = []

    for page_num, page in enumerate(pdf_reader.pages):
        text = page.extract_text()
        if not text:
            continue

        chunks = chunk_text(text)
        for i, chunk in enumerate(chunks):
            all_chunks.append({"chunk_text": chunk, "page": page_num+1})
            ids.append(f"p{page_num+1}_c{i}")

    # Embed with local model
    vectors = []
    embeddings = embed_model.encode([c["chunk_text"] for c in all_chunks])

    for i, emb in enumerate(embeddings):
        vectors.append({
            "id": ids[i],
            "values": emb.tolist(),
            "metadata": all_chunks[i]
        })

    index.upsert(vectors=vectors)
    return jsonify({"message": f"Inserted {len(vectors)} chunks"}), 201