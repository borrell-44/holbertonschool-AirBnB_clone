#!/usr/bin/python3
""" Tests for the BaseModel class  """

from models.base_model import BaseModel
from os.path import exists
import unittest


class TestBaseModel(unittest.TestCase):
    """ Base_model tests """

    def test_save(self):
        """ testing the save function """
        obj = BaseModel()
        self.assertEqual((obj.__class__).__name__, "BaseModel")

    def test_str(self):
        """ testing the str return value"""

    if __name__ == "__main__":
        unittest.main()
