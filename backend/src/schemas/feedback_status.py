# from pydantic import BaseModel, EmailStr, Field
# from datetime import datetime
# from typing import Optional
from enum import Enum


class FeedbackStatus(str, Enum):
    pending = "pending"
    in_progress = "in_progress"
    resolved = "resolved"