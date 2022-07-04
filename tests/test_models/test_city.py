#!/usr/bin/python3

""" Unit Tests for the City class  """

from models.city import City
import unittest


class TestUser(unittest.TestCase):
    """ City tests """

    def test_variables(self):
        """ test if the variables exists inside the class """
        obj = City()
        self.assertEqual(obj.state_id, "")
        self.assertEqual(obj.name, "")

    if __name__ == "__main__":
        unittest.main()
