import uvicorn
from fastapi import FastAPI

from model.models import RememberModel, Query
from utils.youtube_transcript import fetch_transcipt
from utils.create_embedding import sentence_list

from utils.db import *


app = FastAPI()


@app.post("/remember")
def remeber(rememberModel: RememberModel):
    object_list = fetch_transcipt(rememberModel.video_id)

    print("Transcript fetch successful")

    sentences, metadatas = sentence_list(object_list)

    for i, _ in enumerate(sentences):
        try:
            write(text=sentences[i], metadata=metadatas[i])
        except Exception as e:
            print(e)
            return
    
    return {"message":"Task started successfully"}
    

@app.post("/ask")
def ask():
    return


@app.get("/")
async def read_root(text: Query):
    # sentence_encoder.sentence_encoder.encode_query(text)
    return {"message": "Task Started Successfully", "inputText": text}


@app.get("/info")
async def return_model():
    return {"message": "Show model information"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8001)
