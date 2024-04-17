import pymongo
from pymongo import MongoClient

# MongoDB connection details
MONGO_CONNECTION_STRING = "mongodb+srv://jaydenfunk:NpbZAO5utUcSErum@cluster0.zcdxvfn.mongodb.net/"

# Create a MongoDB client
client = pymongo.MongoClient(MONGO_CONNECTION_STRING)

# Access database and collection
db = client["RecipeGenerator"]
collectionI = db["Ingredients"]
collectionR = db["Recipes"]



