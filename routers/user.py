from starlette import status
from typing import Annotated
from datetime import timedelta
from fastapi import Depends, APIRouter, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from core.auth import get_current_user, authenticate_user, create_access_token, bcrypt_context
from sqlalchemy.orm import Session

from database import SessionLocal
from models.user import User
from schemas.user import UserRequest, UpdateUserRequest


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)


@router.get("/users", status_code=status.HTTP_200_OK)
async def user(db: db_dependency):
    return db.query(User).all()


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(db: db_dependency, user_request: UserRequest):
    create_user_model = User(
        username = user_request.username,
        email = user_request.email,
        password = bcrypt_context.hash(user_request.password),
        is_active = user_request.is_active,
        is_admin= user_request.is_admin,
    )

    db.add(create_user_model)
    db.commit()
    return {"message": "User created", "user_id": create_user_model.id}


@router.post("/token")
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: db_dependency):
    access_user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate user.")
    token = create_access_token(access_user.username, access_user.id, timedelta(minutes=20))
    return {"access_token": token, "token_type": "Bearer"}


@router.put("/{user_id}", status_code=status.HTTP_200_OK)
async  def update_user(user_id: int, user_request: UpdateUserRequest,  db: db_dependency):
    search_user_id = db.query(User).filter(User.id == user_id).first()
    if not search_user_id:
        raise HTTPException(status_code=404, detail="User not found")

    search_user_id.username = user_request.username
    search_user_id.email = user_request.email
    search_user_id.is_active = user_request.is_active

    db.add(search_user_id)
    db.commit()
    return {"message": "User updated", "user_id": search_user_id.id}


@router.delete("/{user_id}", status_code=status.HTTP_200_OK)
async def delete_user(user_id: int, db: db_dependency):
    search_user_id = db.query(User).filter(User.id == user_id).first()

    if not search_user_id:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(search_user_id)
    db.commit()