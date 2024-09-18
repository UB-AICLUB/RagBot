import uvicorn
from fastapi import FastAPI

from model.models import RememberModel
from utils.youtube_transcript import fetch_transcipt
from utils.db import add

from typing import Union
from pydantic import BaseModel
# import sentence_encoder


app = FastAPI()

# TODO move this to models file
class Query(BaseModel):
    query: str

@app.post("/remember")
def remeber(rememberModel: RememberModel):
    object_list = fetch_transcipt(rememberModel.video_id)
    
    print("Transcript fetch successful")

    #TODO: Iterating the objects to save data in ChromaDB
    
    return {"message":"Task started successfully"}
    

@app.post("/ask")
def ask():
    return


@app.get("/")
async def read_root(text : Query):
    # sentence_encoder.sentence_encoder.encode_query(text)
    return {"message":"Task Started Successfully", "inputText": text}

@app.get("/info")
async def return_model():
    return {"message": "Show model information"}
  
  
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8001)
