#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}
    classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is None or (f'{cls}' not in type(self).classes):
            return FileStorage.__objects
        else:
            filtered = {}
            filtered.update(FileStorage.__objects)
            for key in filtered.keys():
                if f'{cls}' not in key:
                    type(self).delete(filtered[key])
            return filtered

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        '''
        delete an instance of type obj from the FileStorage
        '''
        if obj is None or (type(obj).__name__ not in type(self).classes):
            return

        # get the name of obj as it's stored in FileStorage.__objects
        name = type(obj).__name__ + '.' + obj.id

        # delete the corresponding object from FileStorage.__objects
        for item in FileStorage.__objects.keys():
            if item == name:
                del FileStorage.__objects[item]
                self.save()
                return
