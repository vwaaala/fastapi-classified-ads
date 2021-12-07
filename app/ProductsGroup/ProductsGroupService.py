from typing import List

import sqlalchemy
from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from ProductsGroup.ProductsGroupModel import ProductsGroup
from ProductsGroup.ProductsGroupSchema import CreateProductsGroup


def get_all_users(db: Session, skip: int = 0, limit: int = 12) -> List[ProductsGroup]:
    return db.query(ProductsGroup).offset(skip).limit(limit).all()


def get_user(db: Session, username) -> ProductsGroup:
    return db.query(ProductsGroup).filter(ProductsGroup.username == username).one()


def create_product_group(product_group: CreateProductsGroup, db: Session):
    product_group_db_object = ProductsGroup(**product_group.dict())
    db.add(product_group_db_object)
    # noinspection PyUnresolvedReferences
    try:
        db.commit()
        db.refresh(product_group_db_object)
        return product_group_db_object
    except sqlalchemy.exc.IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='User already exists!'
        )
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=Exception
        )
