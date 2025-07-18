from fastapi import APIRouter,Depends,Query,HTTPException
from app.core.deps import get_current_user
from app.db.mongo import db
from app.models.wardrobe_model import WardrobeOut
from typing import List
from bson import ObjectId
router=APIRouter(prefix="/outfit",tags=["Outfit"])
@router.get("/suggest",response_model=List[WardrobeOut])
async def suggest_outfit(weather:str=Query(...),occasion:str=Query(...),user:dict=Depends(get_current_user)):
    query={
        "user_id":str(user["_id"]),
        "weather_tags":weather,
        "occasion":occasion
    }
    items=await db.wardrobe.find(query).to_list(100)
    if not items:
        raise HTTPException(status_code=404,detail="No matching outfits found")
    for item in items:
        item["_id"]=str(item["_id"])
    return items
