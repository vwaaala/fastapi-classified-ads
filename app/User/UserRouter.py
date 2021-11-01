from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.User import UserSchema, UserService

router = APIRouter(
    prefix='/users',
    tags=['User'],
)


@router.get('/', response_model=List[UserSchema.UserBase])
async def get_users(skip: int = 0, limit: int = 12, db: Session = Depends(get_db)):
    users = UserService.get_all_users(db, skip, limit)
    return users


@router.get('/{username}', response_model=UserSchema.UserBase)
async def read_item(username: str, db: Session = Depends(get_db)):
    return UserService.get_user(db, username)


@router.post('/', response_model=UserSchema.UserBase)
async def create_user(user: UserSchema.CreateUser, db: Session = Depends(get_db)):
    return UserService.create_user(user, db)
