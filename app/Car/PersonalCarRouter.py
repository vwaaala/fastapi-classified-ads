from fastapi import APIRouter, Depends, Request, Form, UploadFile
from pydantic import Json
from sqlalchemy.orm import Session

from Car import PersonalCarSchema, PersonalCarService, PersonalCarModel
from Helpers.db_item_listing import get_all_items,get_all_modified
from Helpers.query_param_helper import cleanup_query,cleanup_query_modified
from Helpers.utils import validate_json_schema, get_schema_valiation_obejct
from Image import ImageService
from database import get_db

router = APIRouter(
    prefix="/cars",
    tags=["Car"],
)


# noinspection PyShadowingBuiltins
@router.get("/", response_model=PersonalCarSchema.CarsResponse)
async def get_all_cars(request: Request, page: int = 1, limit: int = 12, sort: str = 'id', order: str ='desc',
                       db: Session = Depends(get_db)):
    query_params, sort, order = cleanup_query_modified(request.query_params, sort, order)

    result = get_all_modified(PersonalCarModel.Car, PersonalCarSchema.CarsResponse, db, page, limit, sort, query_params,order)

    return result


@router.post("/", response_model=PersonalCarSchema.Car)
def create_car(data: Json = Form(...), image: UploadFile = Form(None), db: Session = Depends(get_db)):
    data = validate_json_schema(data, PersonalCarSchema.CreateCar)
    return PersonalCarService.create_car(db, data, image)


@router.put("/{car_id}", response_model=PersonalCarSchema.Car)
def update_car(car_id: int, data: Json = Form(...), image: UploadFile = Form(None), db: Session = Depends(get_db)):
    data = validate_json_schema(data, PersonalCarSchema.CreateCar)
    return PersonalCarService.update_car(car_id, car=data, db=db, image=image)


@router.post("/{car_id}/images")
def add_image(car_id: int, image: UploadFile = Form(...), db: Session = Depends(get_db)):
    return ImageService.save_image(car_id, PersonalCarModel.CarImage, image, db=db)


@router.get("/categories")
async def get_categories(db: Session = Depends(get_db)):
    result = PersonalCarService.get_categories(db)

    return result


# noinspection PyShadowingBuiltins
@router.get("/filters")
async def get_categories(request: Request, db: Session = Depends(get_db), ):
    result = PersonalCarService.get_filters(
        db,
        request.query_params
    )

    return result

@router.get("/get_master_Data")
async def get_master_Data(request: Request, db: Session = Depends(get_db), ):
    result = PersonalCarService.get_master_Data(
        db,
        request.query_params
    )

    return result



@router.get("/fields")
def find_fields(db: Session = Depends(get_db)):
    return get_schema_valiation_obejct(db, PersonalCarSchema.CreateCar,
                                       PersonalCarService.get_filters)


@router.get("/{car_id}", response_model=PersonalCarSchema.Car)
async def get_car(car_id: int, db: Session = Depends(get_db)):
    return PersonalCarService.get_car(db, car_id)


@router.delete("/{car_id}", response_model=PersonalCarSchema.Car)
async def archive_car(car_id: int, db: Session = Depends(get_db)):
    return PersonalCarService.archive_car(db, car_id)
