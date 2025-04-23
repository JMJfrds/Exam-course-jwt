from fastapi import FastAPI
from database import Base, engine
from routers import user
from routers import lessons
from routers import courses
# from routers import comrate


Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(user.router)
app.include_router(courses.router)
app.include_router(lessons.router)
# app.include_router(comrate.router)

