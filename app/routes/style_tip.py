from fastapi import APIRouter,Query
from typing import List,Optional
from app.schema.style_tips import StyleTip
router=APIRouter()
STYLE_TIPS = [
    {"tip": "Wear light colors during summer to stay cool.", "tags": ["summer"]},
    {"tip": "Layer your clothes in winter for warmth and flexibility.", "tags": ["winter"]},
    {"tip": "Avoid suede shoes in rainy weather.", "tags": ["rainy"]},
    {"tip": "Formal shoes go best with suits or trousers.", "tags": ["formal"]},
    {"tip": "Add a belt to give your outfit a structured look.", "tags": ["casual", "formal"]},
    {"tip": "Pair your jackets with neutral shirts for balance.", "tags": ["winter", "rainy"]},
]
@router.get("/style-tips", response_model=List[StyleTip])
def get_style_tips(
    tags: Optional[List[str]] = Query(None, description="Filter by tags like 'summer', 'formal'")
):
    if tags:
        return [tip for tip in STYLE_TIPS if any(tag in tip["tags"] for tag in tags)]
    return STYLE_TIPS