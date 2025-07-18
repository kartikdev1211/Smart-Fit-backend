from fastapi import APIRouter,Depends,HTTPException
from app.core.deps import get_current_user
from app.models.user_model import UserOut
from app.db.mongo import db
router=APIRouter(prefix="/user",tags=["User"])
@router.get("/profile", response_model=UserOut)
async def get_user_profile(current_user=Depends(get_current_user)):
    # current_user is just {"sub": "email@example.com"} from JWT token
    user = await db.users.find_one({"email": current_user["sub"]})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user["_id"] = str(user["_id"])  # Convert ObjectId to string if needed
    return user