from fastapi import APIRouter, Depends, Request, UploadFile, Form
from pydantic import Json
from sqlalchemy.orm import Session

from Helpers.db_item_listing import get_all_items,get_all_modified
from Helpers.query_param_helper import cleanup_query,cleanup_query_modified
from Helpers.utils import validate_json_schema, get_schema_valiation_obejct
from Image import ImageService
from Machinery import MachinerySchema, MachineryService, MachineryModel
from database import get_db

router = APIRouter(
    prefix="/machinery",
    tags=["Machinery"],
)


@router.get("/", response_model=MachinerySchema.MachineriesResponse)
async def get_all_machineries(request: Request, page: int = 1, limit: int = 12, sort: str = 'id', order: str = 'desc',
                              db: Session = Depends(get_db)):
    query_params, sort ,order= cleanup_query_modified(request.query_params, sort, order)

    result = get_all_modified(MachineryModel.Machinery, MachinerySchema.MachineriesResponse, db, page, limit, sort,
                           query_params,order)

    return result


@router.post("/", response_model=MachinerySchema.Machinery)
def create_machinery(data: Json = Form(...), image: UploadFile = Form(None), db: Session = Depends(get_db)):
    data = validate_json_schema(data, MachinerySchema.CreateMachinery)
    return MachineryService.create_machinery(db, data, image)


@router.put("/{machinery_id}", response_model=MachinerySchema.Machinery)
def update_machinery(machinery_id: int, data: Json = Form(...), image: UploadFile = Form(None),
                     db: Session = Depends(get_db)):
    data = validate_json_schema(data, MachinerySchema.CreateMachinery)
    return MachineryService.update_machinery(machinery_id, machinery=data, db=db, image=image)


@router.post("/{machinery_id}/images")
def add_image(machinery_id: int, image: UploadFile = Form(...), db: Session = Depends(get_db)):
    return ImageService.save_image(machinery_id, MachineryModel.MachineryImage, image, db=db)


@router.get("/categories")
def get_categories(db: Session = Depends(get_db)):
    result = MachineryService.get_categories(db)

    return result

@router.get("/get_master_Data")
async def get_master_Data(request: Request, db: Session = Depends(get_db), ):
    result = MachineryService.get_master_Data(
        db,
        request.query_params
    )

    return result

@router.get("/fields")
def find_fields(db: Session = Depends(get_db)):
    return get_schema_valiation_obejct(db, MachinerySchema.CreateMachinery, MachineryService.get_categories)


@router.get("/{machinery_id}", response_model=MachinerySchema.Machinery)
def get_machinery(machinery_id: int, db: Session = Depends(get_db)):
    return MachineryService.get_machinery(db, machinery_id)


@router.delete("/{machinery_id}", response_model=MachinerySchema.Machinery)
async def archive_machinery(machinery_id: int, db: Session = Depends(get_db)):
    return MachineryService.archive_machinery(db, machinery_id)
