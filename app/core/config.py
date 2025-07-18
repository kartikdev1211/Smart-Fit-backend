class Config:
    MONGO_URI = "mongodb+srv://kartikkysp12:6Rg4mBmNs8wnh73t@cluster0.7hhmgql.mongodb.net/"
    JWT_SECRET = "e770bd46c5c6e9eca06d8a1026176fcd8a26e83baafaa32ff74011d9a50056f3"
    JWT_ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
    CORS_ORIGINS = ['http://localhost', 'http://127.0.0.1']
