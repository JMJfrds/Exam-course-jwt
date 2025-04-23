from typing import Annotated
from starlette import status
from fastapi import Depends, APIRouter, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from database import SessionLocal

from schemas.lesson import LessonRequest
from models.lesson import Lessons

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

router = APIRouter(
    prefix = "/lesson",
    tags = ["Lessons"]
)


@router.get("/", status_code=status.HTTP_200_OK)
async def get_all_lessons(db: db_dependency):
    return db.query(Lessons).all()


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_course(db: db_dependency, lesson_request: LessonRequest):
    create_lesson_model = Lessons(
        course_id = lesson_request.course_id,
        title = lesson_request.title,
        video_url = lesson_request.video_url,
        content = lesson_request.content,
    )

    db.add(create_lesson_model)
    db.commit()
    return {"message": "Lesson created", "lesson_id": create_lesson_model.id}


@router.put("/{lesson_id}", status_code=status.HTTP_200_OK)
async def update_course(lesson_id: int, course_request: LessonRequest, db: db_dependency):
    search_lesson_id = db.query(Lessons).filter(Lessons.id == lesson_id).first()
    if not search_lesson_id:
        raise HTTPException(status_code=404, detail="Course not found")


    search_lesson_id.title = course_request.title
    search_lesson_id.video_url = course_request.video_url
    search_lesson_id.content = course_request.content

    db.add(search_lesson_id)
    db.commit()


@router.delete("/{user_id}", status_code=status.HTTP_200_OK)
async def delete_user(lesson_id: int, db: db_dependency):
    search_user_id = db.query(Lessons).filter(Lessons.id == lesson_id).first()

    if not search_user_id:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(search_user_id)
    db.commit()