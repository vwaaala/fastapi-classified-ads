# noinspection PyPackageRequirements
import datetime
from typing import List

from pydantic import BaseModel


class MachineryImage(BaseModel):
    image: str

    class Config:
        orm_mode = True


class MachineryBase(BaseModel):
    title: str
    group: str = None
    type: str = None
    manufacturer: str = None
    cash: float
    location: str = None
    archived: bool = False
    user: str = None


class MachineryShortResponse(MachineryBase):
    id: int
    link: str = None
    image: str = None

    class Config:
        orm_mode = True


class CreateMachinery(MachineryBase):
    manufacturer: str = None
    technical_condition: str = None
    year: str = None
    location: str = None
    description: str = None
    leasing: str
    credit: str


class Machinery(CreateMachinery):
    id: int
    image: str = None
    images: List[MachineryImage] = []
    created_at: datetime.datetime
    last_updated: datetime.datetime
    link: str = None

    class Config:
        orm_mode = True


class MachineriesResponse(BaseModel):
    items: List[MachineryShortResponse]
    pages: int
    limit: int
    page: int
