from fastapi import APIRouter,Depends,HTTPException
from bson import ObjectId
from app.models.wardrobe_model import WardrobeCreate,WardrobeOut,WardrobeUpdate
from app.db.mongo import db
from app.core.deps import get_current_user
router=APIRouter(prefix="/wardrobe",tags=["wardrobe"])
@router.post("/",response_model=WardrobeCreate)
async def add_item(item:WardrobeCreate,current_user:str=Depends(get_current_user)):
    data=item.dict()
    data["user_id"]=current_user
    result=await db.wardrobe.insert_one(data)
    data["_id"]=str(result.inserted_id)
    return data
@router.get("/",response_model=list[WardrobeOut])
async def get_all_items(current_user:str=Depends(get_current_user)):
    items=await db.wardrobe.find({"user_id":current_user}).to_list(100)
    for item in items:
        item["_id"]=str(item["_id"])
    return items
@router.get("/{item_id}",response_model=WardrobeOut)
async def get_item(item_id:str,current_user:str=Depends(get_current_user)):
    item=await db.wardrobe.find_one({"_id":ObjectId(item_id),"user_id":current_user})
    if not item:
        raise HTTPException(status_code=404,detail="Item not found")
    item["_id"]=str(item["_id"])
    return item
@router.put("/{item_id}")
async def update_item(
    item_id: str,
    item_data: WardrobeUpdate,  # <- use a different name than the function
    current_user: dict = Depends(get_current_user)
):
    result = await db.wardrobe.update_one(
        {"_id": ObjectId(item_id), "user_id": current_user},
        {"$set": item_data.dict(exclude_unset=True)}
    )
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Item not found or not modified")
    return {"msg": "Item updated successfully"}
@router.delete("/{item_id}")
async def delete_item(item_id:str,current_user:str=Depends(get_current_user)):
    result=await db.wardrobe.delete_one({"_id":ObjectId(item_id),"user_id":current_user})
    if result.deleted_count==0:
        raise HTTPException(status_code=404,detail="Item not found")
    return {"detail":"Item deleted successfully"}