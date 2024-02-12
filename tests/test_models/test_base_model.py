#!/usr/bin/python3
"""
Unittest for BaseModel class
"""
import json
import unittest
from models.base_model import BaseModel
from datetime import datetime
import models
import sys
import os
import pep8


class TestBaseModel(unittest.TestCase):
    """
    classss for base model test
    """

    @classmethod
    def setUpClass(cls):
        cls.base = BaseModel()
        cls.base.name = "XX"
        cls.base.my_number = 100

    @classmethod
    def tear_Down_Class(cls):
        del cls.base
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_style_check(self):
        style = pep8.StyleGuide(quiet=True)
        pp = style.check_files(['models/base_model.py'])
        self.assertEqual(pp.total_errors, 0, "fix pep8")

    def test_checking(self):
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_attributes(self):
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_initialization(self):
        self.assertTrue(isinstance(self.base, BaseModel))

    def test_save(self):
        self.base.save()
        self.assertNotEqual(self.base.created_at, self.base.updated_at)

    def test_to_dict_func(self):
        base1_dict = self.base.to_dict()
        self.assertEqual(self.base.__class__.__name__, 'BaseModel')
        self.assertIsInstance(base1_dict['created_at'], str)
        self.assertIsInstance(base1_dict['updated_at'], str)
    pass


if __name__ == '__main__':
    unittest.main()
