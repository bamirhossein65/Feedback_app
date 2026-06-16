from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Optional
from src.schemas.feedback_status import FeedbackStatus

class FeedbackBase(BaseModel):
    name: Optional[str] = Field(None, max_length=100)
    email: Optional[EmailStr] = Field(None)
    message: str = Field(..., max_length=1000)

class FeedbackCreate(FeedbackBase):
    pass

class FeedbackUpdateStatus(BaseModel):
    status: FeedbackStatus

class FeedbackResponse(FeedbackBase):
    id: int
    status: FeedbackStatus
    created_at: datetime

    model_config = {"from_attributes": True}