import datetime

from sqlalchemy import Column, Integer, Text, ForeignKey, DateTime, DECIMAL, Boolean
from sqlalchemy.orm import relationship

from database import Base


class Machinery(Base):
    __tablename__ = "machinery"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(Text)
    group = Column(Text)
    type = Column(Text)
    manufacturer = Column(Text)
    technical_condition = Column(Text)
    year = Column(Integer)
    location = Column(Text)
    description = Column(Text)
    cash = Column(DECIMAL)
    leasing = Column(DECIMAL)
    credit = Column(DECIMAL)
    link = Column(Text)
    image = Column(Text)
    archived = Column(Boolean, default=False)
    last_updated = Column(DateTime, default=datetime.datetime.utcnow)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    user = Column(Text)
    images = relationship('MachineryImage', primaryjoin="Machinery.id==MachineryImage.item_id")


class MachineryImage(Base):
    __tablename__ = "machineries_images"

    id = Column(Integer, primary_key=True, index=True)
    item_id = Column(Integer, ForeignKey('machinery.id'))
    image = Column(Text)

