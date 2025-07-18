from pymongo import MongoClient
import os

# MongoDB connection URL and DB name
MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://kartikkysp12:6Rg4mBmNs8wnh73t@cluster0.7hhmgql.mongodb.net/")
MONGO_DB_NAME = "smart_fit"

# Create Mongo client and DB instance
client = MongoClient(MONGO_URL)
db = client[MONGO_DB_NAME]
