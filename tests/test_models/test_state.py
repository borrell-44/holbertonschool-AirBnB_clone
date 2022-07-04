#!/usr/bin/python3

""" Unit Tests for the User class  """

from models.state import State
import unittest


class TestState(unittest.TestCase):
    """ State tests """

    def test_variables(self):
        """ test if the variables exists inside the class """
        obj = State()
        self.assertEqual(obj.name, "")

    if __name__ == "__main__":
        unittest.main()
