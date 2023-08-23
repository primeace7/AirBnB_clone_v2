#!/usr/bin/python3
"""Place Module for HBNB project"""
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship
from os import getenv


class Place(BaseModel, Base):
    """"A place to stay
    Also inherits from alchemy base
    Atrributes:
        __tablename__: represents the table name, places
        city_id: represents a column containing a string
        user_id: represents a column containing a string
        name: represents a column containing a string
        description: represents a column containing a string
        number_rooms: represents a column containing an integer
        number_bathrooms: represents a column containing an integer
        price_by_night: represents a column containing an integer
        latitude: represents a column containing a float
        longitude: represents a column containing a float
    """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    reviews = relationship("Review", backref="place", cascade="delete")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def reviews(self):
            """Getter attribute reviews that returns the list of Review
            instances with place_id equals to the current Place.id
            """
            list_of_reviews = []
            for review in models.storage.all(Review).values():
                if review.place.id == self.id:
                    list_of_reviews.append(review)
            return list_of_reviews
