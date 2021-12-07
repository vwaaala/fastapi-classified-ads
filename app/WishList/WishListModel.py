from sqlalchemy import Column, Integer, Text

from database import Base


class WishList(Base):
    __tablename__ = "wishlist"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    item_id = Column(Integer)
    item_type = Column(Text)
