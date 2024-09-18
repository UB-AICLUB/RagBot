import chromadb

client = chromadb.Client()

collection = client.create_collection("my_collection")

def add(text: str):
    #TODO: Implement CRUD operation - add
    return