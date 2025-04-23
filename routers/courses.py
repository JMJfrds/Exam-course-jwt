from typing import Annotated
from starlette import status
from fastapi import Depends, APIRouter, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from database import SessionLocal
from schemas.user import UserRequest
from schemas.courses import CourseRequest, UpdateCourseRequest
from models.courses import Courses


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

router = APIRouter(
    prefix = "/course",
    tags = ["Courses"]
)


@router.get("/courses/", status_code = status.HTTP_200_OK)
def get_courses(db: db_dependency):
    return db.query(Courses).all()


@router.post("/course/", status_code=status.HTTP_201_CREATED)
async def create_course(db: db_dependency, course_request: CourseRequest):
    create_course_model = Courses(
        title = course_request.title,
        description = course_request.description,
        author_id = course_request.author_id,
    )
    db.add(create_course_model)
    db.commit()
    return {"message": "Course created", "course": create_course_model}


@router.put("/{course_id}/", status_code=status.HTTP_200_OK)
async def update_course(course_id: int, course_request: UpdateCourseRequest, db: db_dependency):
    search_course_id = db.query(Courses).filter(Courses.id == course_id).scalar()
    if not search_course_id:
        raise HTTPException(status_code=404, detail="Course not found")

    search_course_id.title = course_request.title
    search_course_id.description = course_request.description

    db.add(search_course_id)
    db.commit()
    return {"message": "User updated", "course": search_course_id}


@router.delete("/{user_id}/", status_code=status.HTTP_200_OK)
async def delete_user(course_id: int, db: db_dependency):
    search_course_id = db.query(Courses).filter(Courses.id == course_id).first()
    if not search_course_id:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(search_course_id)
    db.commit()