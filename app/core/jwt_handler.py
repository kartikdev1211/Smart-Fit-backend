from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt
from app.core.config import Config
def create_access_token(data:dict, expire_delta:Optional[timedelta]=None):
    to_encode=data.copy()
    if expire_delta:
        expire=datetime.utcnow()+expire_delta
    else:
        expire=datetime.utcnow()+timedelta(days=9999)
    to_encode.update({"exp":expire})
    return jwt.encode(to_encode,Config.JWT_SECRET,algorithm=Config.JWT_ALGORITHM)
def verify_token(token:str):
    try:
        payload=jwt.decode(token,Config.JWT_SECRET,algorithms=[Config.JWT_ALGORITHM])
        return payload
    except JWTError:
        return None