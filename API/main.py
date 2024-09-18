from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
# import sentence_encoder


app = FastAPI()

class Query(BaseModel):
    query: str

@app.get("/")
async def read_root(text : Query):
    # sentence_encoder.sentence_encoder.encode_query(text)
    return {"message":"Task Started Successfully", "inputText": text}

@app.get("/info")
async def return_model():
    return {"message": "Show model information"}
