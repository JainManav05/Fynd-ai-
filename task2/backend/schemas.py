from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ReviewBase(BaseModel):
    rating: int
    review_text: str

class ReviewCreate(ReviewBase):
    pass

class ReviewResponse(ReviewBase):
    id: int
    ai_response: Optional[str] = None
    ai_summary: Optional[str] = None
    ai_action: Optional[str] = None
    created_at: datetime

    class Config:
        from_attributes = True
