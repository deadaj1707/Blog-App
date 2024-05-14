from pymongo import MongoClient
MONGO_URI: str="mongodb+srv://username:password@cluster0.brdbnmc.mongodb.net/notes"
conn= MongoClient(MONGO_URI)
