from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import Config

client = AsyncIOMotorClient(Config.MONGO_URI)
db = client.smart_fit