from fastapi import APIRouter, Depends, Request, Form, UploadFile
from pydantic import Json
from sqlalchemy.orm import Session

from Helpers.db_item_listing import get_all_items,get_all_modified
from Helpers.query_param_helper import cleanup_query,cleanup_query_modified
from Helpers.utils import validate_json_schema, get_schema_valiation_obejct
from Image import ImageService
from Truck import TruckModel, TruckSchema, TruckService
from database import get_db

router = APIRouter(
    prefix="/trucks",
    tags=["Truck"],
)


# noinspection PyShadowingBuiltins
@router.get("/", response_model=TruckSchema.TrucksResponse)
async def get_all_trucks(request: Request, page: int = 1, limit: int = 12, sort: str = 'id', order: str = 'desc',
                         db: Session = Depends(get_db)):
    query_params, sort, order= cleanup_query_modified(request.query_params, sort,order)
    result = get_all_modified(TruckModel.Truck, TruckSchema.TrucksResponse, db, page, limit, sort, query_params,order)

    return result


@router.post("/", response_model=TruckSchema.Truck)
def create_truck(data: Json = Form(...), image: UploadFile = Form(None), db: Session = Depends(get_db)):
    data = validate_json_schema(data, TruckSchema.CreateTruck)
    return TruckService.create_truck(db, data, image)


@router.put("/{truck_id}", response_model=TruckSchema.Truck)
def update_truck(truck_id: int, data: Json = Form(...), image: UploadFile = Form(None), db: Session = Depends(get_db)):
    data = validate_json_schema(data, TruckSchema.CreateTruck)
    return TruckService.update_truck(truck_id, truck=data, db=db, image=image)


@router.post("/{truck_id}/images")
def add_image(truck_id: int, image: UploadFile = Form(...), db: Session = Depends(get_db)):
    return ImageService.save_image(truck_id, TruckModel.TruckImage, image, db=db)


@router.get("/categories")
async def get_categories(db: Session = Depends(get_db)):
    result = TruckService.get_categories(db)

    return result


# noinspection PyShadowingBuiltins
@router.get("/filters")
async def get_filters(request: Request, db: Session = Depends(get_db), ):
    result = TruckService.get_filters(
        db,
        request.query_params
    )

    return result

@router.get("/get_master_Data")
async def get_master_Data(request: Request, db: Session = Depends(get_db), ):
    result = TruckService.get_master_Data(
        db,
        request.query_params
    )

    return result

@router.get("/fields")
def find_fields(db: Session = Depends(get_db)):
    return get_schema_valiation_obejct(db, TruckSchema.CreateTruck, TruckService.get_filters)


@router.get("/{truck_id}", response_model=TruckSchema.Truck)
async def get_truck(truck_id: int, db: Session = Depends(get_db)):
    return TruckService.get_truck(db, truck_id)


@router.delete("/{truck_id}", response_model=TruckSchema.Truck)
async def archive_truck(truck_id: int, db: Session = Depends(get_db)):
    return TruckService.archive_truck(db, truck_id)
