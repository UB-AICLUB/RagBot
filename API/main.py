import uvicorn
from fastapi import FastAPI

from model.models import RememberModel
from utils.youtube_transcript import fetch_transcipt
from utils.db import add

app = FastAPI()

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8001, reload=True)

@app.post("/remember")
def remeber(rememberModel: RememberModel):
    object_list = fetch_transcipt(rememberModel.video_id)
    
    print("Transcript fetch successful")

    #TODO: Iterating the objects to save data in ChromaDB
    
    return {"message":"Task started successfully"}
    

@app.post("/ask")
def ask():
    return
