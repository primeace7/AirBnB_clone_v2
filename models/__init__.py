#!/usr/bin/python3
"""This module instantiates an object of Storage either filestorage or db

if  equal to db:
    Create an instance of DBStorage and store it in the variable storage
else:
    Create an instance of FileStorage and store it in the variable storage
"""
from os import getenv


if getenv("HBNB_TYPE_STORAGE") == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
