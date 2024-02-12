#!/usr/bin/python3
"""
Unittest for Place class
"""
import unittest
import os
import pep8
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.place2 = Place()
        cls.place2.city_id = "Rabat"
        cls.place2.user_id = "saad"
        cls.place2.name = "Agdal"
        cls.place2.description = "Avenue france"
        cls.place2.number_rooms = 0
        cls.place2.number_bathrooms = 0
        cls.place2.max_guest = 0
        cls.place2.price_by_night = 0
        cls.place2.latitude = 0.0
        cls.place2.longitude = 0.0
        cls.place2.amenity_ids = []

    @classmethod
    def tearDownClass(cls):
        del cls.place2
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_style(self):
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/place.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_if_is_subclass(self):
        self.assertTrue(issubclass(self.place1.__class__, BaseModel), True)

    def test_checking_functions(self):
        self.assertIsNotNone(Place.__doc__)

    def test_has_attributes(self):
        self.assertTrue('id' in self.place2.__dict__)
        self.assertTrue('created_at' in self.place2.__dict__)
        self.assertTrue('updated_at' in self.place2.__dict__)
        self.assertTrue('city_id' in self.place2.__dict__)
        self.assertTrue('user_id' in self.place2.__dict__)
        self.assertTrue('name' in self.place2.__dict__)
        self.assertTrue('description' in self.place2.__dict__)
        self.assertTrue('number_rooms' in self.place2.__dict__)
        self.assertTrue('number_bathrooms' in self.place2.__dict__)
        self.assertTrue('max_guest' in self.place2.__dict__)
        self.assertTrue('price_by_night' in self.place2.__dict__)
        self.assertTrue('latitude' in self.place2.__dict__)
        self.assertTrue('longitude' in self.place2.__dict__)
        self.assertTrue('amenity_ids' in self.place2.__dict__)

    def test_attributes_are_strings(self):
        self.assertEqual(type(self.place2.city_id), str)
        self.assertEqual(type(self.place2.user_id), str)
        self.assertEqual(type(self.place2.name), str)
        self.assertEqual(type(self.place2.description), str)
        self.assertEqual(type(self.place2.number_rooms), int)
        self.assertEqual(type(self.place2.number_bathrooms), int)
        self.assertEqual(type(self.place2.max_guest), int)
        self.assertEqual(type(self.place2.price_by_night), int)
        self.assertEqual(type(self.place2.latitude), float)
        self.assertEqual(type(self.place2.longitude), float)
        self.assertEqual(type(self.place2.amenity_ids), list)

    def test_save(self):
        self.place2.save()
        self.assertNotEqual(self.place2.created_at, self.place2.updated_at)

    def test_to_dict(self):
        self.assertEqual('to_dict' in dir(self.place2), True)


if __name__ == "__main__":
    unittest.main()
