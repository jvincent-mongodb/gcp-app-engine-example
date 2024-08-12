import os
import certifi
import json
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pymongo import MongoClient
from typing import Annotated

from index import index_view

app = FastAPI()

password = os.environ.get('MONGO_PASSWORD')
username = os.environ.get('MONGO_USERNAME')

mongo_uri = f'mongodb+srv://{username}:{password}@cluster1-pri.ncz2p.mongodb-dev.net/?retryWrites=true&w=majority&appName=Cluster1'

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
