from fastapi import APIRouter, Depends, HTTPException
from app.core.deps import get_current_user
from app.models.user_model import UserOut
from app.db.mongo import db

router = APIRouter(prefix="/user", tags=["User"])

@router.get("/profile", response_model=UserOut)
async def get_user_profile(current_user: dict = Depends(get_current_user)):
    email = current_user.get("sub")
    if not email:
        raise HTTPException(status_code=400, detail="Invalid token")

    user = await db.users.find_one({"email": email})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return {
        "_id": str(user["_id"]),
        "full_name": user["full_name"],
        "email": user["email"]
    }
