import os
import certifi
import json
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pymongo import MongoClient
from typing import Annotated

from index import index_view

app = FastAPI()

mongo_uri = <add Atlas connection string here>

client = MongoClient(mongo_uri, tlsCAFile=certifi.where())
db = client.sample_mflix
collection = db.comments

@app.get("/")
async def index():
    return HTMLResponse(content=index_view, status_code=200)
    
@app.get("/get-doc")
async def index():
    r = collection.find_one({"name":"Mercedes Tyler"})
    data = {'name': r['name'], 'text':r['text']}

    return json.dump(data)
