import cloudinary
import cloudinary.uploader
from app.core.config import Config
import logging

logger = logging.getLogger(__name__)

try:
    # Configure Cloudinary
    cloudinary.config(
        cloud_name=Config.CLOUDINARY_CLOUD_NAME,
        api_key=Config.CLOUDINARY_API_KEY,
        api_secret=Config.CLOUDINARY_API_SECRET
    )
    logger.info("Cloudinary configured successfully")
    logger.info(f"Cloud name: {Config.CLOUDINARY_CLOUD_NAME}")
    logger.info(f"API Key: {Config.CLOUDINARY_API_KEY[:10]}...")
except Exception as e:
    logger.error(f"Failed to configure Cloudinary: {str(e)}")
    raise 