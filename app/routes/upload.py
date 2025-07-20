from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from app.core.deps import get_current_user
from app.core.cloudinary_config import cloudinary
import logging
import traceback

router = APIRouter(prefix="/upload", tags=["Upload"])
logger = logging.getLogger(__name__)

@router.post("/image")
async def upload_image(
    file: UploadFile = File(...),
    current_user: dict = Depends(get_current_user)
):
    """
    Upload an image to Cloudinary
    """
    try:
        logger.info(f"Starting image upload for user: {current_user['sub']}")
        logger.info(f"File details: {file.filename}, {file.content_type}, {file.size} bytes")
        
        # Validate file type
        if not file.content_type.startswith('image/'):
            logger.warning(f"Invalid file type: {file.content_type}")
            raise HTTPException(status_code=400, detail="File must be an image")
        
        # Validate file size (max 10MB)
        if file.size and file.size > 10 * 1024 * 1024:
            logger.warning(f"File too large: {file.size} bytes")
            raise HTTPException(status_code=400, detail="File size must be less than 10MB")
        
        # Read file content
        file_content = await file.read()
        logger.info(f"File content read successfully: {len(file_content)} bytes")
        
        # Upload to Cloudinary
        logger.info("Attempting Cloudinary upload...")
        upload_result = cloudinary.uploader.upload(
            file_content,
            folder="smart_fit",
            public_id=f"{current_user['sub']}_{file.filename}",
            overwrite=True
        )
        
        logger.info(f"Image uploaded successfully for user {current_user['sub']}")
        logger.info(f"Cloudinary response: {upload_result}")
        
        return {
            "success": True,
            "url": upload_result["secure_url"],
            "public_id": upload_result["public_id"],
            "filename": file.filename
        }
        
    except Exception as e:
        logger.error(f"Error uploading image: {str(e)}")
        logger.error(f"Traceback: {traceback.format_exc()}")
        raise HTTPException(status_code=500, detail=f"Failed to upload image: {str(e)}")

@router.delete("/image/{public_id}")
async def delete_image(
    public_id: str,
    current_user: dict = Depends(get_current_user)
):
    """
    Delete an image from Cloudinary
    """
    try:
        logger.info(f"Attempting to delete image: {public_id}")
        
        # Delete from Cloudinary
        result = cloudinary.uploader.destroy(public_id)
        
        if result["result"] == "ok":
            logger.info(f"Image deleted successfully: {public_id}")
            return {"success": True, "message": "Image deleted successfully"}
        else:
            logger.error(f"Cloudinary delete failed: {result}")
            raise HTTPException(status_code=400, detail="Failed to delete image")
            
    except Exception as e:
        logger.error(f"Error deleting image: {str(e)}")
        logger.error(f"Traceback: {traceback.format_exc()}")
        raise HTTPException(status_code=500, detail="Failed to delete image") 