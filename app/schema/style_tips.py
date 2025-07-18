from pydantic import BaseModel
from typing import List
class StyleTip(BaseModel):
    tip:str
    tags:List[str]