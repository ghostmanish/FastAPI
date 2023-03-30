from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional


app = FastAPI()

message = None

Student = {
    "user1": {
        "id": 1,
        "name": "Manish",
        "age": 22,
        "message": "Hello Manish",
        "role": "Admin"
    },
    "user2": {
        "id": 2,
        "name": "Ravi",
        "age": 23,
        "message": "Hello Ravi",
        "role": "User"
    },
    "user3": {
        "id": 3,
        "name": "Rahul",
        "age": 24,
        "message": "Hello Rahul",
        "role": "User"
    }
}

class Student_class(BaseModel):
    id: int
    name: str
    age: int
    message: str
    role: str
class Student_class_update(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    age: Optional[int] = None
    message: Optional[str] = None
    role: Optional[str] = None
@app.get("/")
def read_root():
    return {"Hello": "Manish"}

@app.get("/items")
def create_item():
    return Student

@app.get("/items/{user_id}")
def read_item(user_id: str, q: Optional[str] = None):
    if user_id in Student:
        return Student[user_id]
    else:
        return {"Error": "User not found"}
    
@app.post("/update-items/{user_id}")
def update_item(user_id: str, item: Student_class):
    if user_id in Student:
        return {"Error": "User already exists"}
    else:
        Student[user_id] = item
        return Student[user_id]
    
@app.delete("/delete-items/{user_id}")
def delete_item(user_id: str):
    if user_id not in Student:
        return {"Error": "User not found"}
    else:
        del Student[user_id]
        return {"Message": "User deleted successfully"}
    
@app.put("/update-user/{user_id}")
def update_item(user_id: str, item: Student_class_update):
    if user_id not in Student:
        return {"Error": "User not found"}
    else:
        if item.id != None:
            Student[user_id].id = item.id
        if item.name != None:
            Student[user_id].name = item.name
        if item.age != None:
            Student[user_id].age = item.age
        if item.message != None:
            Student[user_id].message = item.message
        if item.role != None:
            Student[user_id].role = item.role
        return Student[user_id]
    