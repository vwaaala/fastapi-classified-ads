from sqlalchemy.orm import Session

from Helpers.db_item_listing import get_unique_values
from Image import ImageService
from Truck import TruckSchema, TruckModel
from MasterData import MasterDataSchema, MasterDataModel


def create_truck(db: Session, truck: TruckSchema.CreateTruck, image=None):
    db_truck = TruckModel.Truck(**truck.dict())
    db.add(db_truck)
    db.commit()
    db.refresh(db_truck)

    if image:
        db_image = ImageService.save_image(db_truck.id, TruckModel.TruckImage, image, db)
        db_truck.image = db_image.image
        db.commit()
        db.refresh(db_truck)

    return db_truck


def get_truck(db: Session, truck_id: int):
    result = db.query(TruckModel.Truck).filter(TruckModel.Truck.id == truck_id).one()

    return result


def get_categories(db: Session):
    # brands_id = db.query(TruckModel.Truck.id_brand).distinct().subquery()
    # # brands = get_unique_values(TruckModel.Truck, db, TruckModel.Truck.brand)
    # brands = db.query(MasterDataModel.ProductsBrand).filter(MasterDataModel.ProductsBrand.id.in_(brands_id))
    # brands = [row for row in brands]

    brands = get_unique_values(TruckModel.Truck, db, TruckModel.Truck.brand, "", 100)
    models = get_unique_values(TruckModel.Truck, db, TruckModel.Truck.model)
    years = get_unique_values(TruckModel.Truck, db, TruckModel.Truck.year)
    types = get_unique_values(TruckModel.Truck, db, TruckModel.Truck.type)

    years.sort()
    # sort
    return {
        "brand": brands,
        "model": models,
        "year": years,
        "type": types,
    }

def get_master_Data(db: Session, query=None, result_limit=10):
    brands = db.query(MasterDataModel.ProductsBrand).filter(MasterDataModel.ProductsBrand.id_group == 2).all()
    brands_id = [brand.id for brand in brands]
    models = db.query(MasterDataModel.ProductsModel).filter(MasterDataModel.ProductsModel.id_brand.in_(brands_id)).all()
    sub_groups = db.query(MasterDataModel.ProductsSubGroup).filter(MasterDataModel.ProductsSubGroup.id_group == 2).all()
    return {
        "brands": brands,
        "models": models,
        "types": sub_groups,
    }

def get_filters(db: Session, query=None, result_limit=10):
    brands = get_unique_values(TruckModel.Truck, db, TruckModel.Truck.brand, query=query, limit=10)

    if query and 'brand' in query:
        result_limit = 99

    models = get_unique_values(TruckModel.Truck, db, TruckModel.Truck.model, query=query, limit=result_limit)
    years = get_unique_values(TruckModel.Truck, db, TruckModel.Truck.year, query=query, limit=result_limit)
    types = get_unique_values(TruckModel.Truck, db, TruckModel.Truck.type, query=query, limit=result_limit)

    years.sort()

    return {
        "brand": brands,
        "model": models,
        "year": years,
        "type": types,
    }


def update_truck(truck_id: int, truck: TruckSchema.Truck, db: Session, image=None):
    db_truck_object = get_truck(db, truck_id)

    for var, value in vars(truck).items():
        setattr(db_truck_object, var, value) if value else None

    if image:
        db_image = ImageService.save_image(truck_id, TruckModel.TruckImage, image, db)
        db_truck_object.image = db_image.image

    db.commit()
    db.refresh(db_truck_object)

    return db_truck_object


def archive_truck(db: Session, truck_id: int):
    db_car_object = get_truck(db, truck_id)
    db_car_object.archived = not db_car_object.archived

    db.commit()

    return db_car_object
