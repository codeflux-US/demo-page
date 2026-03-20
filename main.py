from fastapi import FastAPI, Depends, Header
from auth import router
from security import verify_token

app = FastAPI()

app.include_router(router)

def auth_required(authorization: str = Header()):
    try:
        return verify_token(authorization)
    except:
        return None

@app.get("/api/data")
def secure_api(user=Depends(auth_required)):
    if not user:
        return {"error": "Unauthorized"}
    return {"msg": "Secure Data", "user": user}
