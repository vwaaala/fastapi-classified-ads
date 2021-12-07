import datetime

from sqlalchemy import Column, Integer, Text, ForeignKey, DateTime, DECIMAL, Boolean
from sqlalchemy.orm import relationship

from database import Base
from MasterData import MasterDataModel

class TruckBase(Base):
    __tablename__ = "trucks"

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


class Truck(TruckBase):
    archived = Column(Boolean, default=False)
    axles = Column(Integer)
    moc = Column(Text)
    description = Column(Text)
    leasing = Column(DECIMAL)
    credit = Column(DECIMAL)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    images = relationship('TruckImage', primaryjoin="Truck.id==TruckImage.item_id")
    # brand_info = relationship('MasterDataModel.ProductsBrand', primaryjoin="Truck.id_brand==MasterDataModel.ProductsBrand.id")
    # type_info = relationship('MasterDataModel.ProductsSubGroup', primaryjoin="Truck.id_sub_group==MasterDataModel.ProductsSubGroup.id")
    # model_info = relationship('MasterDataModel.ProductsModel',
    #                          primaryjoin="Truck.id_model==MasterDataModel.ProductsModel.id")


class TruckImage(Base):
    __tablename__ = "truck_images"

    id = Column(Integer, primary_key=True, index=True)
    item_id = Column(Integer, ForeignKey('trucks.id'))
    image = Column(Text)
