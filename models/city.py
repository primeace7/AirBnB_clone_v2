#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import String
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, represents a city for the mysqldatabase

    Inherits from both BaseModel and Base(sqlalchemy)

    Attributes:
        __tablename__: represents the table name, cities
        name: represents a column containing a string
        state_id: epresents a column containing a string
    """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
