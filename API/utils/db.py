import uuid
import chromadb


def get_connection():
    """
    Returns a connection object to our ChromaDB instance.
    Connection parameters are hardcoded for now.
    """
    client = chromadb.Client()
    return client

def write(text, metadata, collection_name="default_collection"):
    """
    Writes embeddings, text, and metadata to ChromaDB.
    
    Args:
    - embedding (list): The embedding vector
    - text (str): The original text
    - metadata (dict): Additional metadata
    - collection_name (str): Name of the collection to write to
    """
    client = get_connection()
    collection = client.get_or_create_collection(name=collection_name)
    
    # Assuming each item needs a unique ID, we're using the text as the ID here
    # In a real-world scenario, you might want to use a more robust ID generation method
    collection.add(
        documents=[text],
        metadatas=[metadata],
        ids=[str(uuid.uuid4())]
    )
