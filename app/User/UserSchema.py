# noinspection PyPackageRequirements
from pydantic import BaseModel


class UserBase(BaseModel):
    name: str
    username: str
    type: str = 'user'

    class Config:
        orm_mode = True


class CreateUser(UserBase):
    password: str


class UserResponse(UserBase):
    id: int

    class Config:
        orm_mode = True


class User(CreateUser):
    id: int

    class Config:
        orm_mode = True
