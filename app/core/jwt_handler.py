from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt
from app.core.config import SECRET_KEY,ALGORITHM
def create_access_token(data:dict, expire_delta:Optional[timedelta]=None):
    to_encode=data.copy()
    if expire_delta:
        expire=datetime.utcnow()+expire_delta
    else:
        expire=datetime.utcnow()+timedelta(days=9999)
    to_encode.update({"exp":expire})
    return jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
def verify_token(token:str):
    try:
        payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None