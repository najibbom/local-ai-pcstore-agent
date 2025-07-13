# Import Ollama embeddings, Chroma vector store, and Document class
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os
import pandas as pd


# Load the CSV file containing PC store reviews
df = pd.read_csv('realistic_pcstore_reviews.csv')


# Initialize the embedding model (can be changed to other Ollama embedding models)
embeddings = OllamaEmbeddings(model='mxbai-embed-large')


# Directory for ChromaDB persistence
db_location = './chroma_db'


# Only add documents if the vector DB does not exist yet
add_documents = not os.path.exists(db_location)


# Build Document objects from the CSV rows and add to ChromaDB
if add_documents:
    documents = []
    ids = []
    for i, row in df.iterrows():
        document = Document(
            page_content=row["Title"] + " " + row["Review"],
            metadata={"rating": row["Rating"], "date": row["Date"]},
            id=str(i)
        )
        ids.append(str(i))
        documents.append(document)

# Create the Chroma vector store (persistent)
vector_store = Chroma(
    collection_name="pcstore_reviews",
    embedding_function=embeddings,
    persist_directory=db_location,
)


# Add documents to the vector store if needed
if add_documents:
    vector_store.add_documents(documents=documents ,ids=ids)


# Expose a retriever for semantic search (top 5 relevant reviews)
retriever = vector_store.as_retriever(
    search_kwargs={"k": 5}
)
