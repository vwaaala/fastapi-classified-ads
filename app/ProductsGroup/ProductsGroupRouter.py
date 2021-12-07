from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from ProductsGroup import ProductsGroupSchema, ProductsGroupService

router = APIRouter(
    prefix="/products-group",
    tags=["Products Group"],
)


@router.get("/", response_model=List[ProductsGroupSchema.ProductsGroupBase])
async def get_users(skip: int = 0, limit: int = 12, db: Session = Depends(get_db)):
    users = ProductsGroupService.get_all_users(db, skip, limit)

    return users


@router.get("/{user_id}", response_model=ProductsGroupSchema.ProductsGroupBase)
async def read_item(user_id: str):
    return {'Test': user_id}


@router.post("/", response_model=ProductsGroupSchema.ProductsGroupBase)
async def create_product_group(product_group: ProductsGroupSchema.CreateProductsGroup, db: Session = Depends(get_db)):
    return ProductsGroupService.create_product_group(product_group, db)
