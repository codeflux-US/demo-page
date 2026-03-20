from jose import jwt
from datetime import datetime, timedelta

SECRET = "SUPER_SECRET"

def create_token(data):
    payload = data.copy()
    payload["exp"] = datetime.utcnow() + timedelta(minutes=15)
    return jwt.encode(payload, SECRET, algorithm="HS256")

def verify_token(token):
    return jwt.decode(token, SECRET, algorithms=["HS256"])
