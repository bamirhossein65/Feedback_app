from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Optional
from src.schemas.feedback_status import FeedbackStatus

class FeedbackBase(BaseModel):
    name:Optional[str] = Field(None, max_length=100,description="نام فرستنده بازخورد")
    email: Optional[EmailStr] = Field(None, description="ایمیل فرستنده بازخورد")
    status: Optional[FeedbackStatus] = Field(None, description="وضعیت بازخورد")
    message: str = Field(..., max_length=1000, description="متن بازخورد")

class FeedbackCreate(FeedbackBase):
    pass

class FeedbackUpdateStatus(BaseModel):
    status: FeedbackStatus = Field(..., description="وضعیت جدید بازخورد")

class FeedbackResponse(FeedbackBase):
    id:int
    status:FeedbackStatus
    created_at: datetime


    model_config = {"from_attributes": True}

