# noinspection PyPackageRequirements
import datetime
from typing import List

from pydantic import BaseModel


class CarImage(BaseModel):
    image: str

    class Config:
        orm_mode = True


class CarBase(BaseModel):
    title: str
    brand: str
    model: str
    type: str
    year: int
    capacity: str = None
    mileage: str = None
    user: str = None
    cash: float
    archived: bool = False


class CarResponseShort(CarBase):
    id: int
    link: str = None
    image: str = None

    class Config:
        orm_mode = True


class CreateCar(CarBase):
    description: str = None
    location: str = None
    fuel: str = None
    vat: str = None
    leasing: float
    credit: float
    approval: str = None


class Car(CreateCar):
    id: int
    link: str = None
    image: str = None
    images: List[CarImage] = []
    created_at: datetime.datetime
    last_updated: datetime.datetime

    class Config:
        orm_mode = True


class CarsResponse(BaseModel):
    items: List[CarResponseShort]
    pages: int
    limit: int
    page: int
