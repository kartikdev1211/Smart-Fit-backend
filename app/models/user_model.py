from pydantic import BaseModel, EmailStr, Field
from typing import Optional
class UserCreate(BaseModel):
    full_name:str
    email: EmailStr
    password:str
class UserLogin(BaseModel):
    email:EmailStr
    password:str
class UserOut(BaseModel):
    id:str=Field(..., alias="_id")
    full_name: str
    email:EmailStr
    class Config:
        allow_population_by_field_name=True
        arbitrary_types_allowed=True
        json_encoders={
            str:lambda x:str(x)
        }  
class UserWithToken(BaseModel):
    access_token: str
    token_type: str
    user: UserOut 