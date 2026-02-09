import os
from dotenv import load_dotenv
from pymongo import MongoClient

# Load .env from project root
load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

if not MONGO_URI:
    raise ValueError("MONGO_URI is not set in the .env file")

client = MongoClient(MONGO_URI)

db = client["study_planner"]
task_collection = db["tasks"]
