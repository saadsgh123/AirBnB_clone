#!/usr/bin/python3
"""
Unittest for Review class
"""
import unittest
import os
import pep8
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.rev2 = Review()
        cls.rev2.place_id = "Hamid"
        cls.rev2.user_id = "AS"
        cls.rev2.text = "Nice to meet you!"

    @classmethod
    def tear_Down_Class(cls):
        del cls.rev2
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_style_check(self):
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/review.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_if_is_subclass(self):
        self.assertTrue(issubclass(self.rev2.__class__, BaseModel), True)

    def test_checking_for_functions(self):
        self.assertIsNotNone(Review.__doc__)

    def test_attributes_exist(self):
        self.assertTrue('id' in self.rev2.__dict__)
        self.assertTrue('created_at' in self.rev2.__dict__)
        self.assertTrue('updated_at' in self.rev2.__dict__)
        self.assertTrue('place_id' in self.rev2.__dict__)
        self.assertTrue('text' in self.rev2.__dict__)
        self.assertTrue('user_id' in self.rev2.__dict__)

    def test_attributes_are_strings(self):
        self.assertEqual(type(self.rev2.text), str)
        self.assertEqual(type(self.rev2.place_id), str)
        self.assertEqual(type(self.rev2.user_id), str)

    def test_save(self):
        self.rev2.save()
        self.assertNotEqual(self.rev2.created_at, self.rev2.updated_at)

    def test_to_dict(self):
        self.assertEqual('to_dict' in dir(self.rev2), True)


if __name__ == "__main__":
    unittest.main()
