# noinspection PyPackageRequirements
import datetime
from typing import List

from pydantic import BaseModel


class ProductsGroupResponseShort(BaseModel):
    id: int
    title: str = None
    brand: str = None
    group: str = None

    class Config:
        orm_mode = True

class ProductsBrandResponseShort(BaseModel):
    id: int
    title: str = None

    class Config:
        orm_mode = True

class ProductsResponseShort(BaseModel):
    id: int
    title: str = None
    brand: ProductsBrandResponseShort = None
    group: ProductsBrandResponseShort = None
    class Config:
        orm_mode = True


class ProductsGroupResponse(BaseModel):
    items: List[ProductsGroupResponseShort]

class ProductsResponse(BaseModel):
    items: List[ProductsResponseShort]