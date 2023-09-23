#!/usr/bin/python3
"""Defining a new engine DBStorage"""
from os import getenv
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.base_model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker


class DBStorage:
    """ A class representing a new database storage engine

    Private Class Attributes:
        __engine: set to none
        __session: set to none
    """
    __engine = None
    __session = None

    def __init__(self):
        """Initializing the new storage database"""
        user = getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        database = getenv("HBNB_MYSQL_DB")

        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}"
                                      .format(user, password, host, database),
                                      pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Querying all objects types depending on class names

        if cls=None, query all types of objects

        Return: A dictionary
        """
        objects = {}
        if cls:
            query_result = self.__session.query(cls).all()
            for obj in query_result:
                key = f"{cls.__name__}.{obj.id}"
                objects[key] = obj

        else:
            for cls in [User, State, City, Amenity, Place, Review]:
                query_result = self.__session.query(cls).all()
                for obj in query_result:
                    key = f"{cls.__name__}.{obj.id}"
                    objects[key] = obj
        return objects

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Committing all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database (feature of SQLAlchemy)"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """close the session after usage"""
        self.__session.close()
        self.__session.remove()
