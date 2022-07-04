#!/usr/bin/python3
""" Tests for the BaseModel class  """

from models.base_model import BaseModel
from os.path import exists
import unittest


class TestBaseModel(unittest.TestCase):
    """ Base_model tests """

    def test_base_save(self):
        """ testing the save function """
        obj = BaseModel()
        obj.save()
        self.assertEqual(exists("file.json"), True)

    if __name__ == "__main__":
        unittest.main()
