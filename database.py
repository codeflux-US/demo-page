from pymongo import MongoClient

client = MongoClient("YOUR_MONGO_URI")
db = client["secureDB"]
users = db["users"]
