from fastapi import APIRouter, HTTPException
from app.models.user_model import UserCreate, UserLogin, UserWithToken
from app.db.mongo import db
from passlib.hash import bcrypt
from app.core.jwt_handler import create_access_token

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/signup", response_model=UserWithToken)
async def signup(user: UserCreate):
    existing = await db.users.find_one({"email": user.email})
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_pwd = bcrypt.hash(user.password)
    result = await db.users.insert_one({
        "full_name": user.full_name,
        "email": user.email,
        "password": hashed_pwd
    })

    access_token = create_access_token(data={"sub": user.email})

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": {
            "_id": str(result.inserted_id),
            "full_name": user.full_name,
            "email": user.email
        }
    }

@router.post("/login", response_model=UserWithToken)
async def login(user: UserLogin):
    existing = await db.users.find_one({"email": user.email})
    if not existing or not bcrypt.verify(user.password, existing["password"]):
        raise HTTPException(status_code=401, detail="Invalid Credentials")

    access_token = create_access_token(data={"sub": user.email})

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": {
            "_id": str(existing["_id"]),
            "full_name": existing["full_name"],
            "email": existing["email"]
        }
    }
