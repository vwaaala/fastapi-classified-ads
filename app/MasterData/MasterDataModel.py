from sqlalchemy import Column, Integer, Text, Boolean,ForeignKey,DateTime

from database import Base
import datetime
from sqlalchemy.orm import relationship

class ProductsGroup(Base):
    __tablename__ = "fk_group"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(Text)
    title_autopanel = Column(Text)
    identyfikator = Column(Text)
    last_updated = Column(DateTime, default=datetime.datetime.utcnow)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    archived = Column(Boolean, default=False)
    created_by = Column(Text)

class ProductsBrand(Base):
    __tablename__ = "fk_brand"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(Text)
    id_group = Column(Integer, ForeignKey('fk_group.id'))
    archived = Column(Boolean, default=False)
    group_info = relationship('ProductsGroup',
                              primaryjoin="ProductsBrand.id_group==ProductsGroup.id")
    created_by = Column(Text)


class ProductsSubGroup(Base):
    __tablename__ = "fk_sub_group"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(Text)
    id_group = Column(Integer, ForeignKey('fk_group.id'))
    archived = Column(Boolean, default=False)
    group_info = relationship('ProductsGroup',
                             primaryjoin="ProductsSubGroup.id_group==ProductsGroup.id")
    created_by = Column(Text)

class ProductsModel(Base):
    __tablename__ = "fk_model"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(Text)
    id_brand = Column(Integer, ForeignKey('fk_brand.id'))
    archived = Column(Boolean, default=False)
    brand_info = relationship('ProductsBrand',
                              primaryjoin="ProductsModel.id_brand==ProductsBrand.id")
    created_by = Column(Text)

class ProductsTechnicalState(Base):
    __tablename__ = "fk_technical_state"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(Text)
    archived = Column(Boolean, default=False)
    created_by = Column(Text)
