#!/usr/bin/python3

""" file Comments """

import uuid
from datetime import datetime


class BaseModel(object):

    """ class Comments """

    def __init__(self, my_number=0, name="", updated_at=None,
                 id="", created_at=None):
        """ init Comments """
        self.id = str(uuid.uuid4())
        date_now = datetime.now()
        self.created_at = date_now
        self.updated_at = date_now

    def __str__(self):
        """ str Comments """
        name = "[" + str(type(self).__name__) + "]"
        nid = "(" + str(self.id) + ")"
        dic = str(self.__dict__)
        return name + " " + nid + " " + dic

    def to_dict(self):
        """ to_dict Comments """
        dic = self.__dict__.copy()
        dic["__class__"] = str(type(self).__name__)
        dic["updated_at"] = self.updated_at.isoformat()
        dic["created_at"] = self.created_at.isoformat()
        return dic

    def save(self):
        """ save Comments """
        date_now = datetime.now()
        self.updated_at = date_now
