from typing import Annotated
from starlette import status
from fastapi import Depends, APIRouter, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from database import SessionLocal
from models.comrate import Comments, Rating
from schemas.comrate import CommentRequest, RatingRequest

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

router = APIRouter(
    prefix = "/Comment & Ratings",
    tags = ["Comments"]
)

@router.get("/", status_code=status.HTTP_200_OK)
async def get_all_comment(db: db_dependency):
    return db.query(Comments).all()


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_comment(comment_request: CommentRequest,  db: db_dependency):
    create_comment_model = Comments(
        user_id = comment_request.user_id,
        lesson_id = comment_request.lesson_id,
        text = comment_request.text,
        created_at=comment_request.created_at
    )

    db.add(create_comment_model)
    db.commit()
    return {"message": "Comment created", "comment_id": create_comment_model.id}

