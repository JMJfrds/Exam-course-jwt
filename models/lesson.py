from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey

class Lessons(Base):
    __tablename__ = 'lessons'

    id = Column(Integer, primary_key = True, nullable = False)
    course_id = Column(Integer, ForeignKey('courses.id'))
    title = Column(String, unique=True)
    video_url = Column(String)
    content = Column(String)
