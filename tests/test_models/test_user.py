#!/usr/bin/python3
"""
Unittest for User class
"""
import unittest
import os
import pep8
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.user1 = User()
        cls.user1.first_name = "Saad"
        cls.user1.last_name = "Sghouri"
        cls.user1.email = "@gmail.com"
        cls.user1.password = "ALLGOOd"

    @classmethod
    def tear_Down_Class(cls):
        del cls.user1
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_style_check(self):
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/user.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_if_is_subclass(self):
        self.assertTrue(issubclass(self.user1.__class__, BaseModel), True)

    def test_checking_for_functions(self):
        self.assertIsNotNone(User.__doc__)

    def test_attributes_exist(self):
        self.assertTrue('password' in self.user1.__dict__)
        self.assertTrue('first_name' in self.user1.__dict__)
        self.assertTrue('last_name' in self.user1.__dict__)
        self.assertTrue('email' in self.user1.__dict__)
        self.assertTrue('id' in self.user1.__dict__)
        self.assertTrue('created_at' in self.user1.__dict__)
        self.assertTrue('updated_at' in self.user1.__dict__)

    def test_attributes_are_strings(self):
        self.assertEqual(type(self.user1.first_name), str)
        self.assertEqual(type(self.user1.first_name), str)
        self.assertEqual(type(self.user1.email), str)
        self.assertEqual(type(self.user1.password), str)

    def test_save(self):
        self.user1.save()
        self.assertNotEqual(self.user1.created_at, self.user1.updated_at)

    def test_to_dict(self):
        self.assertEqual('to_dict' in dir(self.my_ususer1er), True)


if __name__ == "__main__":
    unittest.main()
