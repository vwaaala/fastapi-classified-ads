from sqlalchemy.orm import Session

from Car import PersonalCarModel
from Machinery import MachineryModel
from Truck import TruckModel


def get_stats(db: Session):
    return {
        "cars": db.query(PersonalCarModel.Car).count(),
        "trucks": db.query(TruckModel.Truck).count(),
        "van": db.query(TruckModel.Truck).count(),
        "machinery": db.query(MachineryModel.Machinery).count(),
    }
