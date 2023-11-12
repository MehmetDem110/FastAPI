from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Snack(Base):
    __tablename__ = "snacks"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String, index=True)


class Soda(Base):
    __tablename__ = "sodas"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    flavor = Column(String, index=True)