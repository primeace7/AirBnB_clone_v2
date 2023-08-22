#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
import models


class BaseModel():
    """A base class for all hbnb models"""
    def __init__(self, *args, **kwargs):
        """This method initantializes three public instance attributes.

        Args:
            *arg(tuple): This is a tuple that contains parameters
            **kwargs(dict): This is a dictionary that contains parameterd and
            their values.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        if kwargs:
            if '__class__' in kwargs:
                kwargs.pop('__class__')
            self.__dict__.update(kwargs)
            try:
                self.created_at = datetime.fromisoformat(self.created_at)
                self.updated_at = datetime.fromisoformat(self.updated_at)
            except Exception as e:
                pass


    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
