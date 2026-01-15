from pymongo import MongoClient
import os

def get_db():
    client = MongoClient(
        host=os.getenv("MONGO_HOST"),
        port=int(os.getenv("MONGO_PORT")),
        username=os.getenv("MONGO_USERNAME"),
        password=os.getenv("MONGO_PASSWORD"),
        authSource=os.getenv("MONGO_AUTH_SOURCE")
    )
    return client[os.getenv("MONGO_DB")]