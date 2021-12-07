import datetime

from sqlalchemy import Column, Integer, Text, ForeignKey, DateTime, DECIMAL, Boolean
from sqlalchemy.orm import relationship

from database import Base


class CarBase(Base):
    __tablename__ = "passenger_cars"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(Text)
    brand = Column(Text)
    model = Column(Text)
    type = Column(Text)
    year = Column(Integer)
    capacity = Column(Text)
    mileage = Column(Text)
    cash = Column(DECIMAL)
    image = Column(Text)
    link = Column(Text)
    user = Column(Text)
    last_updated = Column(DateTime, default=datetime.datetime.utcnow)


class Car(CarBase):
    fuel = Column(Text)
    vat = Column(Text)
    location = Column(Text)
    approval = Column(Text)
    archived = Column(Boolean, default=False)
    description = Column(Text)
    leasing = Column(DECIMAL)
    credit = Column(DECIMAL)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    images = relationship('CarImage', primaryjoin="Car.id==CarImage.item_id")


class CarImage(Base):
    __tablename__ = "passenger_car_images"

    id = Column(Integer, primary_key=True, index=True)
    item_id = Column(Integer, ForeignKey('passenger_cars.id'))
    image = Column(Text)
