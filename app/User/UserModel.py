from sqlalchemy import Column, Integer, Text, CHAR

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(Text, unique=True)
    name = Column(Text(255))
    type = Column(Text(255))
    password = Column(CHAR(60))
