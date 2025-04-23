from database import Base
from datetime import datetime

class CommentRequest(Base):

    user_id: int
    lesson_id: int
    text: str
    created_at: datetime

class RatingRequest(Base):

    user_id: int
    lesson_id: int
    stars: int

