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


    if __name__ == "__main__":
        unittest.main()
