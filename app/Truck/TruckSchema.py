# noinspection PyPackageRequirements
import datetime
from typing import List

from pydantic import BaseModel


class TruckImage(BaseModel):
    image: str

    class Config:
        orm_mode = True


class TruckBase(BaseModel):
    title: str
    brand: str = None
    model: str = None
    type: str = None
    year: int
    cash: float
    capacity: str = None
    mileage: str = None
    user: str = None
    archived: bool = False

class MasterDataResponse(BaseModel):
    id: int
    title: str = None

    class Config:
        orm_mode = True

class SubGroupResponse(BaseModel):
    id: int
    title: str = None

    class Config:
        orm_mode = True

class TruckResponseShort(TruckBase):
    id: int
    link: str = None
    image: str = None

    class Config:
        orm_mode = True


class CreateTruck(TruckBase):
    description: str = None
    axles: str = None
    leasing: str = None
    credit: str = None


class Truck(CreateTruck):
    id: int
    link: str = None
    image: str = None
    images: List[TruckImage] = []
    created_at: datetime.datetime
    last_updated: datetime.datetime
    # brand_info: MasterDataResponse = None
    # type_info: MasterDataResponse = None
    # model_info: MasterDataResponse = None

    class Config:
        orm_mode = True



class TrucksResponse(BaseModel):
    items: List[TruckResponseShort]
    pages: int
    limit: int
    page: int
