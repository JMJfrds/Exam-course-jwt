from database import Base
from sqlalchemy import Column, String, Integer, ForeignKey


class Courses(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key = True, nullable = False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey('users.id'))