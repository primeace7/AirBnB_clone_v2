#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column
from sqlalchemy import String
import models
from models.city import City
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ Represent a state for the database and also inherits from sqlachemy

    Attributes:
        __tablename__: represents the table name, states
        name: represents a column containing a string
        cities:  must represent a relationship with the class City.
        If the State object is deleted, all linked City objects must be
        automatically deleted.
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="delete")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """Getter attribute cities that returns the list of City instances
            with state_id equals to the current State.id
            """
            list_of_cities = []
            for city in models.storage.all(City).values():
                if city.state_id == self.id:
                    list_of_cities.append(city)
            return list_of_cities
