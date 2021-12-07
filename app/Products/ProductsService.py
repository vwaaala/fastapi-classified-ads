from sqlalchemy.orm import Session

from Car import PersonalCarModel, PersonalCarSchema
from Helpers.db_item_listing import get_unique_values
from Image import ImageService


def update_car(car_id: int, car: PersonalCarSchema.Car, db: Session, image=None):
    db_car_object = get_car(db, car_id)

    for var, value in vars(car).items():
        setattr(db_car_object, var, value) if value else None

    if image:
        db_image = ImageService.save_image(car_id, PersonalCarModel.CarImage, image, db)
        db_car_object.image = db_image.image

    db.commit()
    db.refresh(db_car_object)

    return db_car_object


def create_car(db: Session, car: PersonalCarSchema.CreateCar, image=None):
    db_car = PersonalCarModel.Car(**car.dict())
    db.add(db_car)
    db.commit()
    db.refresh(db_car)

    if image:
        db_image = ImageService.save_image(db_car.id, PersonalCarModel.CarImage, image, db)
        db_car.image = db_image.image
        db.commit()
        db.refresh(db_car)

    return db_car


def get_car(db: Session, car_id: int):
    result = db.query(PersonalCarModel.Car).filter(PersonalCarModel.Car.id == car_id).one()

    return result


def get_categories(db: Session):
    brands = get_unique_values(PersonalCarModel.Car, db, PersonalCarModel.Car.brand)
    models = get_unique_values(PersonalCarModel.Car, db, PersonalCarModel.Car.model)
    years = get_unique_values(PersonalCarModel.Car, db, PersonalCarModel.Car.year)
    types = get_unique_values(PersonalCarModel.Car, db, PersonalCarModel.Car.type)

    years.sort()

    return {
        "brand": brands,
        "model": models,
        "year": years,
        "type": types,
    }


def get_filters(db: Session, query=None, result_limit=10):
    brands = get_unique_values(PersonalCarModel.Car, db, PersonalCarModel.Car.brand, query=query, limit=result_limit)

    if query and 'brand' in query:
        result_limit = 99

    models = get_unique_values(PersonalCarModel.Car, db, PersonalCarModel.Car.model, query=query, limit=result_limit)
    years = get_unique_values(PersonalCarModel.Car, db, PersonalCarModel.Car.year, query=query, limit=result_limit)
    types = get_unique_values(PersonalCarModel.Car, db, PersonalCarModel.Car.type, query=query, limit=result_limit)

    years.sort()

    return {
        "brand": brands,
        "model": models,
        "year": years,
        "type": types,
    }


def archive_car(db: Session, car_id: int):
    db_car_object = get_car(db, car_id)
    db_car_object.archived = not db_car_object.archived

    db.commit()

    return db_car_object
