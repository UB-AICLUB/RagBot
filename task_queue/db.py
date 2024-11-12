import chromadb
from chromadb.config import Settings

def get_connection():
    """
    Returns a connection object to our ChromaDB instance.
    Connection parameters are hardcoded for now.
    """
    client = chromadb.Client(Settings(
        chroma_db_impl="duckdb+parquet",
        persist_directory="/path/to/persist"  # Replace with actual path
    ))
    return client

def write(embedding, text, metadata, collection_name="default_collection"):
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
        embeddings=[embedding],
        documents=[text],
        metadatas=[metadata],
        ids=[text[:100]]  # Using first 100 chars of text as ID, adjust as needed
    )

def retrieve(embedding, n=5, filter=None, collection_name="default_collection"):
    """
    Retrieves the n closest embeddings along with their metadata.
    
    Args:
    - embedding (list): The query embedding vector
    - n (int): Number of results to retrieve
    - filter (dict): Optional filter for the query
    - collection_name (str): Name of the collection to query
    
    Returns:
    - list of dicts, each containing:
        - 'id': ID of the item
        - 'text': Original text
        - 'metadata': Associated metadata
        - 'distance': Distance from the query embedding
    """
    client = get_connection()
    collection = client.get_collection(name=collection_name)
    
    results = collection.query(
        query_embeddings=[embedding],
        n_results=n,
        where=filter
    )
    
    # Format the results
    formatted_results = []
    for i in range(len(results['ids'][0])):
        formatted_results.append({
            'id': results['ids'][0][i],
            'text': results['documents'][0][i],
            'metadata': results['metadatas'][0][i],
            'distance': results['distances'][0][i]
        })
    
    return formatted_results
