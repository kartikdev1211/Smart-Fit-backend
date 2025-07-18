from pydantic import BaseModel, Field
from typing import List, Optional

class WardrobeCreate(BaseModel):
    name: str
    category: str
    color: Optional[str]
    image_url: Optional[str]
    weather_tags: List[str]
    occasion: Optional[str]  # Added field

class WardrobeUpdate(BaseModel):
    name: Optional[str]
    category: Optional[str]
    color: Optional[str]
    image_url: Optional[str]
    weather_tags: Optional[List[str]]
    occasion: Optional[str]  # Added field

class WardrobeOut(WardrobeCreate):
    id: str = Field(..., alias="_id")

    class Config:
        allow_population_by_field_name = True
