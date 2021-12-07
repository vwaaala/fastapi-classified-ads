from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from Auth.AuthService import authenticate_user, create_access_token, get_current_user
from User.UserSchema import UserResponse
from database import get_db

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.get("/me", response_model=UserResponse)
async def get_current_user(current_user: str = Depends(get_current_user)):
    return current_user


@router.post("/token")
async def auth_token(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(db, form_data)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"}
        )

    access_token = create_access_token({
        "sub": user.username,
        "id": user.id,
        "type": user.type,
        "username": user.username,
        "name": user.name,
    })
    # response.set_cookie(key="access_token", value=f"Bearer {access_token}", httponly=True,
    #                     domain=['http://localhost:8000', 'http://localhost:8080'])

    return {"access_token": access_token, "token_type": "bearer"}
