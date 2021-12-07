import datetime

from sqlalchemy import Column, Integer, Text, ForeignKey, DateTime, DECIMAL, Boolean
from sqlalchemy.orm import relationship

# from database import Base
# from ProductsGroup import ProductsGroupModel

# class ProductsBase(Base):
#     __tablename__ = "products"

#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(Text)
#     year_of_production = Column(Integer)
#     id_brand = Column(Integer, ForeignKey('fk_brand.id'))
#     id_group = Column(Integer, ForeignKey('fk_group.id'))
#     id_sub_group = Column(Integer, ForeignKey('fk_sub_group.id'))
#     capacity = Column(Integer)
#     model_description = Column(Text)
#     price = Column(DECIMAL)
#     engine_type = Column(Text)
#     last_updated = Column(DateTime, default=datetime.datetime.utcnow)


# class Products(ProductsBase):
#     brand = relationship('ProductsBrand', primaryjoin="Products.id_brand==ProductsBrand.id")
#     group = relationship('ProductsGroupModel.ProductsGroup', primaryjoin="Products.id_group==ProductsGroupModel.ProductsGroup.id")
#     sub_group = relationship('ProductsSubGroup', primaryjoin="Products.id_sub_group==ProductsSubGroup.id")


# # class ProductsGroup(Base):
# #     __tablename__ = "fk_group"

# #     id = Column(Integer, primary_key=True, index=True)
# #     title = Column(Text)
# #     title_autopanel = Column(Text)
# #     identyfikator = Column(Text)


# # class ProductsBrand(Base):
# #     __tablename__ = "fk_brand"

# #     id = Column(Integer, primary_key=True, index=True)
# #     title = Column(Text)
# #     id_group = Column(Integer, ForeignKey('ProductsGroup.id'))


# # class ProductsSubGroup(Base):
# #     __tablename__ = "fk_sub_group"

# #     id = Column(Integer, primary_key=True, index=True)
# #     title = Column(Text)
# #     id_group = Column(Integer, ForeignKey('ProductsGroup.id'))
