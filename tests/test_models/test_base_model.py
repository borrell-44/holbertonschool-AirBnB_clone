#!/usr/bin/python3
""" Tests for the BaseModel class  """

from models.base_model import BaseModel
from os.path import exists
import unittest


class TestBaseModel(unittest.TestCase):
    """ Base_model tests """

    def test_class_name(self):
        """ testing the save function """
        obj = BaseModel()
        self.assertEqual((obj.__class__).__name__, "BaseModel")

    def test_save(self):
        """ testing if the save functions exists """
        obj = BaseModel()
        self.assertEqual(obj.save(), None)

    def test_to_dict(self):
        """ test the return value of to_dict """
        obj = BaseModel()
        self.assertEqual(type(obj.to_dict()), dict)

    def test_id(self):
        """ test id existence and type """
        obj = BaseModel()
        self.assertEqual(type(obj.id), str)

    def test_str(self):
        """ test __str__ return value type """
        obj = BaseModel()
        name = "[" + str(type(obj).__name__) + "]"
        nid = "(" + str(obj.id) + ")"
        dic = str(obj.__dict__)
        value = name + " " + nid + " " + dic
        self.assertEqual(obj.__str__(), value)


    if __name__ == "__main__":
        unittest.main()
