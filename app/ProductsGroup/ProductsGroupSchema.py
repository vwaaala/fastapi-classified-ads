# noinspection PyPackageRequirements
from pydantic import BaseModel


class ProductsGroupBase(BaseModel):
    id: int
    title: str
    title_autopanel: str = None
    identyfikator: str = None
    

    class Config:
        orm_mode = True


class CreateProductsGroup(ProductsGroupBase):
    pass


class ProductsGroupResponse(BaseModel):
    id: int

    class Config:
        orm_mode = True


class ProductsGroup(CreateProductsGroup):
    id: int

    class Config:
        orm_mode = True
