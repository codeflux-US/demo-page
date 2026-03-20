from fastapi import APIRouter, HTTPException
from passlib.hash import bcrypt
from database import users
from security import create_token

router = APIRouter()

@router.post("/signup")
def signup(data: dict):
    hashed = bcrypt.hash(data["password"])
    users.insert_one({
        "username": data["username"],
        "password": hashed
    })
    return {"msg": "User created"}

@router.post("/login")
def login(data: dict):
    user = users.find_one({"username": data["username"]})
    if not user or not bcrypt.verify(data["password"], user["password"]):
        raise HTTPException(401, "Invalid")

    token = create_token({"user": user["username"]})
    return {"token": token}
