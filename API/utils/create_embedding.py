from sentence_transformers import SentenceTransformer


def create_embddings(object_list):
    
    model = SentenceTransformer('all-MiniLM-L6-v2')

    sentences, _ = sentence_list(object_list)
    
    embeddings = model.encode(sentences)

    return embeddings

def sentence_list(object_list):
    sentences = []
    metadatas = []

    for obj in object_list:
        sentence = obj.text
        sentences.append(sentence)
        metadata = {
            "start": obj.start,
            "duration": obj.duration
        }
        metadatas.append(metadata)

    return sentences, metadatas