from typing import List
import sqlalchemy
from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.User.UserSchema import CreateUser
from app.User.UserModel import User


def get_all_users(db: Session, skip: int = 0, limit: int = 12) -> List[User]:
    return db.query(User).offset(skip).limit(limit).all()


def get_user(db: Session, username) -> User:
    return db.query(User).filter(User.username == username).one()


def create_user(user: CreateUser, db: Session):
    from app.Auth.AuthService import get_password_hash
    user.password = get_password_hash(user.password)
    user_db_object = User(**user.dict())
    db.add(user_db_object)
    try:
        db.commit()
        db.refresh(user_db_object)
        return user_db_object
    except sqlalchemy.exc.IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='User already exists'
        )
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Failed to create user'
        )
