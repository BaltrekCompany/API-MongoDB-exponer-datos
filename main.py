import os
import json
from fastapi import FastAPI
from pymongo import MongoClient
from bson import json_util
from dotenv import load_dotenv 

load_dotenv() 

app = FastAPI()

# Leemos las variables del .env
MONGO_URI = os.getenv('MONGO_URI')
MONGO_DB = os.getenv('MONGO_DB_NAME')

# Conexión
client = MongoClient(MONGO_URI)
db = client[MONGO_DB]

@app.get("/")
def read_root():
    return {"status": "API Conectada al VPS", "docs": "/docs"}

@app.get("/api/toda-la-data")
def get_all_data():
    # USAMOS LA COLECCIÓN DE TU EJEMPLO:
    collection_name = "testing_michell"
    
    # Traemos todo
    cursor = db[collection_name].find({})
    data = list(cursor)
    
    return json.loads(json_util.dumps(data))