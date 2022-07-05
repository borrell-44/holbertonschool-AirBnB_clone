#!/usr/bin/python3

""" File Storage Tests for the City class  """

from models.engine.file_storage import FileStorage
import unittest


class TestFileStorage(unittest.TestCase):
    """ File Storage tests """

    def test_all_func(self):
        """ test if the all func returns the objects private var """
        obj = FileStorage()
        self.assertEqual((obj.__class__).__name__, "FileStorage")

    if __name__ == "__main__":
        unittest.main()
