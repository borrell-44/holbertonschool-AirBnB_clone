#!/usr/bin/python3

"""
BaseModel takes care of the initialization, serialization
and desarialization  of instances
"""

import uuid
from datetime import datetime


class BaseModel(object):

    """
    BaseModel defines all common attributes/
    methods for others classes
    """

    def __init__(self, *args, **kwargs):
        """ defines public attributes """
        if kwargs:
            self.id = kwargs["id"]
            self.created_at = datetime.strptime(kwargs["created_at"],
                                                '%Y-%m-%dT%H:%M:%S.%f')
            self.updated_at = datetime.strptime(kwargs["updated_at"],
                                                '%Y-%m-%dT%H:%M:%S.%f')
        else:
            self.id = str(uuid.uuid4())
            date_now = datetime.now()
            self.created_at = date_now
            self.updated_at = date_now

    def __str__(self):
        """ returns [<class name>] (<self.id>) <self.__dict__> """
        name = "[" + str(type(self).__name__) + "]"
        nid = "(" + str(self.id) + ")"
        dic = str(self.__dict__)
        return name + " " + nid + " " + dic

    def to_dict(self):
        """ returns a dictionary containing all keys/values of __dict__ """
        dic = self.__dict__.copy()
        dic["__class__"] = str(type(self).__name__)
        dic["updated_at"] = self.updated_at.isoformat()
        dic["created_at"] = self.created_at.isoformat()
        return dic

    def save(self):
        """ updates the public instance attribute updated_at
        with the current datetime """
        date_now = datetime.now()
        self.updated_at = date_now
