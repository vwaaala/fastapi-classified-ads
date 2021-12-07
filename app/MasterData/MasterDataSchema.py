# noinspection PyPackageRequirements
from pydantic import BaseModel
from typing import List
import datetime


class ProductsGroupBase(BaseModel):
    title: str = None
    title_autopanel: str = None
    identyfikator: str = None
    created_by: str = None

    class Config:
        orm_mode = True

class CreateProductsGroup(ProductsGroupBase):
    pass

class ProductsGroup(ProductsGroupBase):
    id : int
    created_at: datetime.datetime
    last_updated: datetime.datetime

    class Config:
        orm_mode = True


class ProductsGroupResponseBase(BaseModel):
    id: int
    title: str = None
    title_autopanel: str = None
    identyfikator: str = None
    archived: bool = False
    class Config:
        orm_mode = True

class ProductsGroupResponse(BaseModel):
    items: List[ProductsGroupResponseBase]
    pages: int
    limit: int
    page: int

######################## Sub-group ####################
class ProductsSubGroupBase(BaseModel):
    title: str = None
    id_group: int = None
    created_by: str = None

    class Config:
        orm_mode = True


class CreateProductsSubGroup(ProductsSubGroupBase):
    pass

class ProductsSubGroupResponseBase(BaseModel):
    id: int
    title: str = None
    archived: bool = False
    id_group: int = None
    group_info: ProductsGroupResponseBase = None
    class Config:
        orm_mode = True

class ProductsSubGroupResponse(BaseModel):
    items: List[ProductsSubGroupResponseBase]
    pages: int
    limit: int
    page: int

##################### Brand #######################
class ProductsBrandBase(BaseModel):
    title: str = None
    id_group: int = None
    created_by: str = None

    class Config:
        orm_mode = True


class CreateProductsBrand(ProductsBrandBase):
    pass

class ProductsBrandResponseBase(BaseModel):
    id: int
    title: str = None
    archived: bool = False
    id_group: int = None
    group_info: ProductsGroupResponseBase = None
    class Config:
        orm_mode = True

class ProductsBrandResponse(BaseModel):
    items: List[ProductsBrandResponseBase]
    pages: int
    limit: int
    page: int


########### Model ##############
class ProductsModelBase(BaseModel):
    title: str = None
    id_brand: int = None
    created_by: str = None

    class Config:
        orm_mode = True


class CreateProductsModel(ProductsModelBase):
    pass

class ProductsModelResponseBase(BaseModel):
    id: int
    title: str = None
    archived: bool = False
    id_brand: int = None
    brand_info: ProductsBrandBase = None
    class Config:
        orm_mode = True

class ProductsModelResponse(BaseModel):
    items: List[ProductsModelResponseBase]
    pages: int
    limit: int
    page: int

########### Model ##############
class ProductsTechStateBase(BaseModel):
    title: str = None
    created_by: str = None
    class Config:
        orm_mode = True


class CreateProductsTechState(ProductsTechStateBase):
    pass

class ProductsTechStateResponseBase(BaseModel):
    id: int
    title: str = None
    archived: bool = False
    class Config:
        orm_mode = True

class ProductsTechStateResponse(BaseModel):
    items: List[ProductsTechStateResponseBase]
    pages: int
    limit: int
    page: int