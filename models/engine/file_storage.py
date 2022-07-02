#!/usr/bin/python3

""" file Comments """

import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage(object):

    """ class Commnets """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ return the dictionary __object """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key """
        name = type(obj).__name__
        key = name + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """ serializes the JSON file to __objects """
        context = {}
        for key in self.__objects.keys():
            context[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w") as f:
            f.write(json.dumps(context))

    def reload(self):
        """ desirializes the JSON file to __objects """
        try:
            with open(self.__file_path, "r") as f:
                content = json.load(f)
                for value in content.values():
                    name = value["__class__"]
                    del value["__class__"]
                    self.new(eval(name)(**value))
        except FileNotFoundError:
            pass
