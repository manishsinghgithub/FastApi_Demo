from enum import Enum
from heapq import heapify

from unicodedata import name
from uuid import UUID, uuid4
from django import db

from fastapi import FastAPI, Path, HTTPException

from model import Gender, Role, User

app=FastAPI()


db:list[User]=[
    User(
        id=uuid4(),
        name="Mainsh",
        gender=Gender.male,
        role=[Role.user, Role.admin]
    ),

    User(
        id=uuid4(),
        name="Rahul",
        gender=Gender.male,
        role=[Role.user]
    ),
]

@app.get("/")
async def read_root():
    return {"Hello":"hey working"}


@app.get("/api/v1/users")
async def fetch_users():
    return db    


@app.post("/api/v1/add-user")
async def addUser(newuser:User):
    db.append(newuser)
    return True


@app.delete("/api/v1/delete")
async def deletelastUser():
    db.pop()
    return True


@app.delete("/api/v1/delete/{uuid}")
async def deletAnUserByUuid(uuid:UUID):
    for user in db:
        if user.id==uuid:
            db.remove(user)
            return f"User with id : {uuid} deleted"
    raise HTTPException(
        status_code=404,
        detail="No user found with this id:"
    )                   