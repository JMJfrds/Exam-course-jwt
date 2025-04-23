from database import Base
from sqlalchemy import Column, String, Integer, Boolean


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key = True, nullable = False)
    username = Column(String, unique = True, nullable = False)
    email = Column(String, unique = True, nullable = False)
    password = Column(String, nullable = False)
    is_active = Column(Boolean, nullable = False)
    is_admin = Column(Boolean, nullable = False)

