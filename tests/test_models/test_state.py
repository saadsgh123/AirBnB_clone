#!/usr/bin/python3
"""
Unittest for State class
"""
import unittest
import os
import pep8
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.state2 = State()
        cls.state2.name = "Hay Riad"

    @classmethod
    def tear_Down_Class(cls):
        del cls.state2
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_style_check(self):
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/state.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_if_is_subclass(self):
        self.assertTrue(issubclass(self.state2.__class__, BaseModel), True)

    def test_checking_for_functions(self):
        self.assertIsNotNone(State.__doc__)

    def test_has_attributes(self):
        self.assertTrue('id' in self.state2.__dict__)
        self.assertTrue('created_at' in self.state2.__dict__)
        self.assertTrue('updated_at' in self.state2.__dict__)
        self.assertTrue('name' in self.state2.__dict__)

    def test_attributes_are_strings(self):
        self.assertEqual(type(self.state2.name), str)

    def test_save(self):
        self.state2.save()
        self.assertNotEqual(self.state2.created_at, self.state2.updated_at)

    def test_to_dict(self):
        self.assertEqual('to_dict' in dir(self.state2), True)


if __name__ == "__main__":
    unittest.main()
