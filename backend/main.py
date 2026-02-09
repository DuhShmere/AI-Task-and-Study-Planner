from fastapi import FastAPI
from pydantic import BaseModel
from backend.database import task_collection
from bson import ObjectId

app = FastAPI()

# Task
class Task(BaseModel):
    title: str
    completed: bool;

# Root
@app.get("/")
def root():
    return {"message": "FastAPI with MongoDB is working"}

# Gets tasks
@app.get("/tasks")
def get_tasks():
    tasks = list(task_collection.find({}, {"_id": 0}))  # exclude MongoDB _id
    return {"tasks": tasks}

#Posts tasks
@app.post("/tasks")
def add_task(task: Task):
    task_collection.insert_one(task.dict())
    return {"message": "Task added", "task": task}
