from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from User.UserSchema import UserBase, CreateUser
from database import get_db
from User import UserSchema, UserService

router = APIRouter(
    prefix="/users",
    tags=["User"],
)


@router.get("/", response_model=List[UserSchema.UserBase])
async def get_users(skip: int = 0, limit: int = 12, db: Session = Depends(get_db)):
    users = UserService.get_all_users(db, skip, limit)

    return users


@router.get("/{user_id}", response_model=UserSchema.UserBase)
async def read_item(user_id: str):
    return {'Test': user_id}


@router.post("/", response_model=UserSchema.UserBase)
async def create_user(user: CreateUser, db: Session = Depends(get_db)):
    return UserService.create_user(user, db)
