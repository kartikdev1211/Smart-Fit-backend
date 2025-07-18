import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017/smartfit')
    JWT_SECRET = os.getenv('JWT_SECRET', 'your_jwt_secret')
    JWT_ALGORITHM = os.getenv('JWT_ALGORITHM', 'HS256')
    ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES', 30))
    CORS_ORIGINS = os.getenv('CORS_ORIGINS', 'http://localhost,http://127.0.0.1').split(',')

SECRET_KEY="e770bd46c5c6e9eca06d8a1026176fcd8a26e83baafaa32ff74011d9a50056f3"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTE=None