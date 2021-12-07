from fastapi import APIRouter, Depends, Request, Form, UploadFile
from pydantic import Json
from sqlalchemy.orm import Session

from Products import ProductsSchema, ProductsService, ProductsModel
# from Helpers.db_item_listing import get_all_items
# from Helpers.query_param_helper import cleanup_query
# from Helpers.utils import validate_json_schema, get_schema_valiation_obejct
# from Image import ImageService
from database import get_db

router = APIRouter(
    prefix="/products",
    tags=["Products"],
)


# noinspection PyShadowingBuiltins
@router.get("/", response_model=ProductsSchema.ProductsResponse)
async def get_all_groups(request: Request, db: Session = Depends(get_db)):
    results = db.query(ProductsModel.Products).all()
    response = ProductsSchema.ProductsResponse(items=results)
    return response

# # noinspection PyShadowingBuiltins
# @router.get("/")
# async def get_all_groups(request: Request, db: Session = Depends(get_db)):
#     results = db.query(ProductsModel.Products).all()
#     return results