import json
from pathlib import Path

import chromadb
from sentence_transformers import SentenceTransformer

# ---------------------------------
# ChromaDB Configuration
# ---------------------------------

client = chromadb.PersistentClient(path="chroma_db")

collection = client.get_or_create_collection(
    name="sports_facts"
)

embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


# ---------------------------------
# Load Sports Facts
# ---------------------------------

def load_data():
    """
    Load sports facts from JSON file.
    """

    data_path = Path("data") / "sports_facts.json"

    try:
        with open(data_path, "r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        raise FileNotFoundError(
            f"Sports facts file not found: {data_path}"
        )

    except json.JSONDecodeError:
        raise ValueError(
            "sports_facts.json contains invalid JSON."
        )


# ---------------------------------
# Initialize ChromaDB
# ---------------------------------

def initialize_database():
    """
    Loads sports facts into ChromaDB.

    This runs only once because duplicate
    insertions are avoided.
    """

    if collection.count() > 0:
        return

    data = load_data()

    ids = []
    documents = []
    embeddings = []
    metadatas = []

    for idx, item in enumerate(data):

        ids.append(str(idx))

        documents.append(item["fact"])

        embeddings.append(
            embedding_model.encode(
                item["fact"]
            ).tolist()
        )

        metadatas.append(
            {
                "sport": item["sport"]
            }
        )

    collection.add(
        ids=ids,
        documents=documents,
        embeddings=embeddings,
        metadatas=metadatas
    )


# ---------------------------------
# Retrieve Relevant Context
# ---------------------------------

def retrieve_context(sport: str, n_results: int = 5):
    """
    Retrieve relevant sports facts from ChromaDB.
    """

    try:

        query_embedding = embedding_model.encode(
            sport
        ).tolist()

        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=n_results,
            where={"sport": sport}
        )

        documents = results.get("documents", [])

        if documents and len(documents) > 0:
            return documents[0]

        return []

    except Exception as e:
        print(f"ChromaDB Retrieval Error: {e}")
        return []