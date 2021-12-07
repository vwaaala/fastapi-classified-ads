from typing import List

import sqlalchemy
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from database import Base
from sqlalchemy import func, asc, desc, or_
from MasterData import MasterDataModel,MasterDataSchema

def get_all_groups(db: Session, skip: int = 0, limit: int = 12) -> List[MasterDataSchema.ProductsGroupResponse]:
    return db.query(MasterDataModel.ProductsGroup).offset(skip).limit(limit).all()

def create_group(db: Session, group: MasterDataSchema.CreateProductsGroup, image=None):
    db_group = MasterDataModel.ProductsGroup(**group.dict())
    db.add(db_group)
    db.commit()
    db.refresh(db_group)

    return db_group

def update_group(group_id: int, group: MasterDataSchema.CreateProductsGroup, db: Session, image=None):
    db_group_object = get_group(db, group_id)

    for var, value in vars(group).items():
        setattr(db_group_object, var, value) if value else None

    db.commit()
    db.refresh(db_group_object)

    return db_group_object

def archive_group(db: Session, group_id: int):
    db_group_object = get_group(db, group_id)
    db_group_object.archived = not db_group_object.archived

    db.commit()

    return db_group_object

def get_group(db: Session, group_id: int):
    result = db.query(MasterDataModel.ProductsGroup).filter(MasterDataModel.ProductsGroup.id == group_id).one()

    return result

def get_all_sub_group(db_model: Base, response_model, db: Session, page: int = 1, limit: int = 12, sort=None,
                  query=None, order=None):
    if query is None:
        query = {}
    if sort is None:
        sort = db_model.last_updated

    orm_query = db.query(db_model)

    if 'q' in query:
        orm_query = orm_query.filter(or_(db_model.id.like(f"%{query['q']}%"), db_model.title.like(f"%{query['q']}%")))
        del query['q']

    orm_query = orm_query.filter_by(**query)

    if order is not None:
        sortInfo = desc(sort) if order == "desc" else asc(sort)
    orm_query = orm_query.order_by(sortInfo)
    results = orm_query.offset((page - 1) * limit).limit(limit).all()


    total = orm_query.count()

    # noinspection PyCallingNonCallable
    response = response_model(items=results, page=page, pages=int(total / limit) + 1, limit=limit)

    return response

def create_sub_group(db: Session, group: MasterDataSchema.CreateProductsGroup, image=None):
    db_group = MasterDataModel.ProductsSubGroup(**group.dict())
    db.add(db_group)
    db.commit()
    db.refresh(db_group)

    return db_group

def update_sub_group(group_id: int, group: MasterDataSchema.CreateProductsGroup, db: Session, image=None):
    db_group_object = get_sub_group(db, group_id)

    for var, value in vars(group).items():
        setattr(db_group_object, var, value) if value else None

    db.commit()
    db.refresh(db_group_object)

    return db_group_object

def archive_sub_group(db: Session, group_id: int):
    db_group_object = get_sub_group(db, group_id)
    db_group_object.archived = not db_group_object.archived

    db.commit()

    return db_group_object

def get_sub_group(db: Session, group_id: int):
    result = db.query(MasterDataModel.ProductsSubGroup).filter(MasterDataModel.ProductsSubGroup.id == group_id).one()

    return result


def create_brand(db: Session, group: MasterDataSchema.CreateProductsBrand, image=None):
    db_brand = MasterDataModel.ProductsBrand(**group.dict())
    db.add(db_brand)
    db.commit()
    db.refresh(db_brand)

    return db_brand

def update_brand(brand_id: int, group: MasterDataSchema.CreateProductsBrand, db: Session, image=None):
    db_group_object = get_brand(db, brand_id)

    for var, value in vars(group).items():
        setattr(db_group_object, var, value) if value else None

    db.commit()
    db.refresh(db_group_object)

    return db_group_object



def archive_brand(db: Session, group_id: int):
    db_brand_object = get_brand(db, group_id)
    db_brand_object.archived = not db_brand_object.archived

    db.commit()

    return db_brand_object

def get_brand(db: Session, group_id: int):
    result = db.query(MasterDataModel.ProductsBrand).filter(MasterDataModel.ProductsBrand.id == group_id).one()

    return result

def create_model(db: Session, group: MasterDataSchema.CreateProductsModel, image=None):
    db_model = MasterDataModel.ProductsModel(**group.dict())
    db.add(db_model)
    db.commit()
    db.refresh(db_model)

    return db_model

def update_model(model_id: int, group: MasterDataSchema.CreateProductsModel, db: Session, image=None):
    db_group_object = get_model(db, model_id)

    for var, value in vars(group).items():
        setattr(db_group_object, var, value) if value else None

    db.commit()
    db.refresh(db_group_object)

    return db_group_object



def archive_model(db: Session, group_id: int):
    db_model_object = get_model(db, group_id)
    db_model_object.archived = not db_model_object.archived

    db.commit()

    return db_model_object

def get_model(db: Session, model_id: int):
    result = db.query(MasterDataModel.ProductsModel).filter(MasterDataModel.ProductsModel.id == model_id).one()

    return result

def create_tech_state(db: Session, group: MasterDataSchema.CreateProductsTechState, image=None):
    db_model = MasterDataModel.ProductsTechnicalState(**group.dict())
    db.add(db_model)
    db.commit()
    db.refresh(db_model)

    return db_model

def update_tech_state(model_id: int, group: MasterDataSchema.CreateProductsTechState, db: Session, image=None):
    db_group_object = get_tech_state(db, model_id)

    for var, value in vars(group).items():
        setattr(db_group_object, var, value) if value else None

    db.commit()
    db.refresh(db_group_object)

    return db_group_object



def archive_tech_state(db: Session, group_id: int):
    db_model_object = get_tech_state(db, group_id)
    db_model_object.archived = not db_model_object.archived

    db.commit()

    return db_model_object

def get_tech_state(db: Session, model_id: int):
    result = db.query(MasterDataModel.ProductsTechnicalState).filter(MasterDataModel.ProductsTechnicalState.id == model_id).one()

    return result
# def get_user(db: Session, username) -> ProductsGroup:
#     return db.query(ProductsGroup).filter(ProductsGroup.username == username).one()
#
#
# def create_product_group(product_group: CreateProductsGroup, db: Session):
#     product_group_db_object = ProductsGroup(**product_group.dict())
#     db.add(product_group_db_object)
#     # noinspection PyUnresolvedReferences
#     try:
#         db.commit()
#         db.refresh(product_group_db_object)
#         return product_group_db_object
#     except sqlalchemy.exc.IntegrityError:
#         raise HTTPException(
#             status_code=status.HTTP_409_CONFLICT,
#             detail='User already exists!'
#         )
#     except Exception:
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             detail=Exception
#         )
