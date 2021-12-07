from datetime import timedelta, datetime

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
# noinspection PyPackageRequirements
from jose import jwt, JWTError
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session

from Auth.AuthSchema import password_context, SECRET_KEY, ALGORITHM, oauth2_scheme, TokenData, \
    ACCESS_TOKEN_EXPIRE_MINUTES
from User.UserService import get_user
from database import get_db


def verify_password(plain_password, hashed_password):
    return password_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return password_context.hash(password)


def authenticate_user(db: Session, form_data: OAuth2PasswordRequestForm):
    try:
        user = get_user(db, form_data.username)
    except NoResultFound:
        return None

    if not verify_password(form_data.password, user.password):
        return None

    return user


def create_access_token(data: dict):
    expires_delta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")

        if username is None:
            raise credentials_exception

        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception

    try:
        user = get_user(db, username=token_data.username)
    except NoResultFound:
        raise credentials_exception

    return user
