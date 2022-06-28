#!/usr/bin/python3

""" file Comments """

import uuid
from datetime import date


class BaseModel(object):

    """ class Comments """

    def __init__(self):
        """ init Comments """
        self.id = str(uuid.uuid4())

    def __str__(self):
        """ str Comments """
        name = "[" + str(self.__name__) + "]"
        nid = "(" + self.id + ")"
        dic = self.__dict__
        return " ".join(name, nid, dic)

    def created_at(self):
        """ created_at Comments """
