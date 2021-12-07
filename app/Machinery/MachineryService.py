from sqlalchemy.orm import Session

from Helpers.db_item_listing import get_unique_values
from Image import ImageService
from Machinery import MachineryModel, MachinerySchema
from MasterData import MasterDataSchema, MasterDataModel

def create_machinery(db: Session, car: MachinerySchema.CreateMachinery, image=None):
    db_item = MachineryModel.Machinery(**car.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)

    if image:
        db_image = ImageService.save_image(db_item.id, MachineryModel.MachineryImage, image, db)
        db_item.image = db_image.image
        db.commit()
        db.refresh(db_item)

    return db_item


def get_machinery(db: Session, item_id: int):
    result = db.query(MachineryModel.Machinery).filter(MachineryModel.Machinery.id == item_id).one()

    return result


def get_categories(db: Session, result_limit=10):
    manufacturers = get_unique_values(MachineryModel.Machinery, db, MachineryModel.Machinery.manufacturer,
                                      limit=result_limit)
    condition = get_unique_values(MachineryModel.Machinery, db, MachineryModel.Machinery.technical_condition,
                                  limit=result_limit)
    years = get_unique_values(MachineryModel.Machinery, db, MachineryModel.Machinery.year, limit=result_limit)

    years = [year for year in years if year]
    years.sort()

    return {
        "manufacturer": manufacturers,
        "technical_condition": condition,
        "year": years
    }


def update_machinery(machinery_id: int, machinery: MachinerySchema.Machinery, db: Session, image=None):
    db_machinery_object = get_machinery(db, machinery_id)

    for var, value in vars(machinery).items():
        setattr(db_machinery_object, var, value) if value else None

    if image:
        db_image = ImageService.save_image(machinery_id, MachineryModel.MachineryImage, image, db)
        db_machinery_object.image = db_image.image

    db.commit()
    db.refresh(db_machinery_object)

    return db_machinery_object


def archive_machinery(db: Session, machinery_id: int):
    db_car_object = get_machinery(db, machinery_id)
    db_car_object.archived = not db_car_object.archived

    db.commit()

    return db_car_object

def get_master_Data(db: Session, query=None, result_limit=10):
    group_id_list=[4,5,6,9,13,14,15,16,17,21,22]
    groups = db.query(MasterDataModel.ProductsGroup).filter(MasterDataModel.ProductsGroup.id.in_(group_id_list)).all() #categories
    types = db.query(MasterDataModel.ProductsSubGroup).filter(MasterDataModel.ProductsSubGroup.id_group.in_(group_id_list)).all()
    brands = db.query(MasterDataModel.ProductsBrand).filter(MasterDataModel.ProductsBrand.id_group.in_(group_id_list)).all()
    technical_states = db.query(MasterDataModel.ProductsTechnicalState).all()

    return {
        "groups":groups,
        "types":types,
        "brands": brands,
        "technical_states": technical_states
    }