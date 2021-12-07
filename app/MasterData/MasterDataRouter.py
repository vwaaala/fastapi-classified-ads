from typing import List

from fastapi import APIRouter, Depends, Request, Form, UploadFile
from sqlalchemy.orm import Session
from Helpers.db_item_listing import get_all_items,get_all_modified
from Helpers.query_param_helper import cleanup_query,cleanup_query_modified
from database import get_db
from pydantic import Json
from MasterData import MasterDataSchema, MasterDataService,MasterDataModel
from Helpers.utils import validate_json_schema, get_schema_valiation_obejct

router = APIRouter(
    prefix="/master-data",
    tags=["Master Data"],
)


@router.get("/groups", response_model=MasterDataSchema.ProductsGroupResponse)
async def get_all_groups(request: Request, page: int = 1, limit: int = 12, sort: str = 'id', order: str ='desc',
                       db: Session = Depends(get_db)):
    requested_query_params=request.query_params
    query_params, sort, order = cleanup_query_modified(requested_query_params, sort, order)

    result = get_all_modified(MasterDataModel.ProductsGroup, MasterDataSchema.ProductsGroupResponse, db, page, limit, sort, query_params, order)

    return result

@router.post("/groups", response_model=MasterDataSchema.CreateProductsGroup)
def create_car(data: Json = Form(...), db: Session = Depends(get_db)):
    data = validate_json_schema(data, MasterDataSchema.CreateProductsGroup)
    return MasterDataService.create_group(db, data)

@router.put("/groups/{group_id}", response_model=MasterDataSchema.CreateProductsGroup)
def update_car(group_id: int, data: Json = Form(...), db: Session = Depends(get_db)):
    data = validate_json_schema(data, MasterDataSchema.CreateProductsGroup)
    return MasterDataService.update_group(group_id, group=data, db=db, image=None)

@router.delete("/groups/{group_id}", response_model=MasterDataSchema.CreateProductsGroup)
async def archive_group(group_id: int, db: Session = Depends(get_db)):
    return MasterDataService.archive_group(db, group_id)

@router.get("/sub-groups", response_model=MasterDataSchema.ProductsSubGroupResponse)
async def get_all_sub_groups(request: Request, page: int = 1, limit: int = 12, sort: str = 'id', order: str ='desc',
                       db: Session = Depends(get_db)):
    requested_query_params=request.query_params
    query_params, sort, order = cleanup_query_modified(requested_query_params, sort, order)

    result = MasterDataService.get_all_sub_group(MasterDataModel.ProductsSubGroup, MasterDataSchema.ProductsSubGroupResponse, db, page, limit, sort, query_params, order)

    return result

@router.post("/sub-groups", response_model=MasterDataSchema.CreateProductsSubGroup)
def create_car(data: Json = Form(...), db: Session = Depends(get_db)):
    data = validate_json_schema(data, MasterDataSchema.CreateProductsSubGroup)
    return MasterDataService.create_sub_group(db, data)

@router.put("/sub-groups/{sub_group_id}", response_model=MasterDataSchema.CreateProductsSubGroup)
def update_car(sub_group_id: int, data: Json = Form(...), db: Session = Depends(get_db)):
    data = validate_json_schema(data, MasterDataSchema.CreateProductsGroup)
    return MasterDataService.update_sub_group(sub_group_id, group=data, db=db, image=None)

@router.delete("/sub-groups/{sub_group_id}", response_model=MasterDataSchema.CreateProductsSubGroup)
async def archive_group(sub_group_id: int, db: Session = Depends(get_db)):
    return MasterDataService.archive_sub_group(db, sub_group_id)

@router.get("/brand", response_model=MasterDataSchema.ProductsBrandResponse)
async def get_all_brands(request: Request, page: int = 1, limit: int = 12, sort: str = 'id', order: str ='desc',
                       db: Session = Depends(get_db)):
    requested_query_params=request.query_params
    query_params, sort, order = cleanup_query_modified(requested_query_params, sort, order)

    result = MasterDataService.get_all_sub_group(MasterDataModel.ProductsBrand, MasterDataSchema.ProductsBrandResponse, db, page, limit, sort, query_params, order)

    return result

@router.post("/brand", response_model=MasterDataSchema.CreateProductsBrand)
def create_brand(data: Json = Form(...), db: Session = Depends(get_db)):
    data = validate_json_schema(data, MasterDataSchema.CreateProductsBrand)
    return MasterDataService.create_brand(db, data)

@router.put("/brand/{brand_id}", response_model=MasterDataSchema.CreateProductsBrand)
def update_brand(brand_id: int, data: Json = Form(...), db: Session = Depends(get_db)):
    data = validate_json_schema(data, MasterDataSchema.CreateProductsBrand)
    return MasterDataService.update_brand(brand_id, group=data, db=db, image=None)

@router.delete("/brand/{brand_id}", response_model=MasterDataSchema.CreateProductsBrand)
async def archive_group(brand_id: int, db: Session = Depends(get_db)):
    return MasterDataService.archive_brand(db, brand_id)


@router.get("/model", response_model=MasterDataSchema.ProductsModelResponse)
async def get_all_models(request: Request, page: int = 1, limit: int = 12, sort: str = 'id', order: str ='desc',
                       db: Session = Depends(get_db)):
    requested_query_params=request.query_params
    query_params, sort, order = cleanup_query_modified(requested_query_params, sort, order)

    result = MasterDataService.get_all_sub_group(MasterDataModel.ProductsModel, MasterDataSchema.ProductsModelResponse, db, page, limit, sort, query_params, order)

    return result

@router.post("/model", response_model=MasterDataSchema.CreateProductsModel)
def create_model(data: Json = Form(...), db: Session = Depends(get_db)):
    data = validate_json_schema(data, MasterDataSchema.CreateProductsModel)
    return MasterDataService.create_model(db, data)

@router.put("/model/{model_id}", response_model=MasterDataSchema.CreateProductsModel)
def update_model(model_id: int, data: Json = Form(...), db: Session = Depends(get_db)):
    data = validate_json_schema(data, MasterDataSchema.CreateProductsModel)
    return MasterDataService.update_model(model_id, group=data, db=db, image=None)

@router.delete("/model/{model_id}", response_model=MasterDataSchema.CreateProductsModel)
async def archive_group(model_id: int, db: Session = Depends(get_db)):
    return MasterDataService.archive_model(db, model_id)

@router.get("/tech-state", response_model=MasterDataSchema.ProductsTechStateResponse)
async def get_all_tech_state(request: Request, page: int = 1, limit: int = 12, sort: str = 'id', order: str ='desc',
                       db: Session = Depends(get_db)):
    requested_query_params=request.query_params
    query_params, sort, order = cleanup_query_modified(requested_query_params, sort, order)

    result = MasterDataService.get_all_sub_group(MasterDataModel.ProductsTechnicalState, MasterDataSchema.ProductsTechStateResponse, db, page, limit, sort, query_params, order)

    return result

@router.post("/tech-state", response_model=MasterDataSchema.CreateProductsTechState)
def create_model(data: Json = Form(...), db: Session = Depends(get_db)):
    data = validate_json_schema(data, MasterDataSchema.CreateProductsTechState)
    return MasterDataService.create_tech_state(db, data)

@router.put("/tech-state/{tech_state_id}", response_model=MasterDataSchema.CreateProductsTechState)
def update_model(tech_state_id: int, data: Json = Form(...), db: Session = Depends(get_db)):
    data = validate_json_schema(data, MasterDataSchema.CreateProductsModel)
    return MasterDataService.update_tech_state(tech_state_id, group=data, db=db, image=None)

@router.delete("/tech-state/{tech_state_id}", response_model=MasterDataSchema.CreateProductsTechState)
async def archive_group(tech_state_id: int, db: Session = Depends(get_db)):
    return MasterDataService.archive_tech_state(db, tech_state_id)