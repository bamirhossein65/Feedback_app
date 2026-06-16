from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from src.config.database import Base
from src.schemas.feedback_status import FeedbackStatus

class Feedback(Base):
    __tablename__ = "feedbacks"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=True)
    email = Column(String, nullable=True)
    message = Column(String, nullable=False)
    status = Column(FeedbackStatus,server_default=FeedbackStatus.pending, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())