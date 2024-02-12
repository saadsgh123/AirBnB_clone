#!/usr/bin/python3
"""
Unittest for Amenity class
"""
import unittest
import os
import pep8
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):

    @classmethod
    def set_up_class(cls):
        cls.amenity2 = Amenity()
        cls.amenity2.name = "Block D"

    @classmethod
    def tear_Down_Class(cls):
        del cls.amenity2
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_style(self):
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/amenity.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_if_is_subclass(self):
        self.assertTrue(issubclass(self.amenity2.__class__, BaseModel), True)

    def test_checking_functions(self):
        self.assertIsNotNone(Amenity.__doc__)

    def test_attributes_exist(self):
        self.assertTrue('id' in self.amenity2.__dict__)
        self.assertTrue('created_at' in self.amenity2.__dict__)
        self.assertTrue('updated_at' in self.amenity2.__dict__)
        self.assertTrue('name' in self.amenity2.__dict__)

    def test_attributes_are_strings(self):
        self.assertEqual(type(self.amenity2.name), str)

    def test_save(self):
        self.amenity2.save()
        self.assertNotEqual(self.amenity2.created_at, self.amenity2.updated_at)

    def test_to_dict(self):
        self.assertEqual('to_dict' in dir(self.amenity2), True)


if __name__ == "__main__":
    unittest.main()
