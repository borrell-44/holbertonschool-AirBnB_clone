#!/usr/bin/python3

""" Unit Tests for the Amenity class  """

from models.amenity import Amenity
import unittest


class TestAmenity(unittest.TestCase):
    """ Amenity tests """

    def test_variables(self):
        """ test if the variables exists inside the class """
        obj = Amenity()
        self.assertEqual(obj.name, "")

    if __name__ == "__main__":
        unittest.main()
