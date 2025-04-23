from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from datetime import datetime

class Comments(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    lesson_id = Column(Integer, ForeignKey('lessons.id'))
    text = Column(String)
    created_at = Column(DateTime, default=datetime.now)


class Rating(Base):
    __tablename__ = 'ratings'

    id = Column(Integer, primary_key = True, nullable = False)
    user_id = Column(Integer, ForeignKey('users.id'))
    lesson_id = Column(Integer, ForeignKey('lessons.id'))
    stars = Column(Integer)