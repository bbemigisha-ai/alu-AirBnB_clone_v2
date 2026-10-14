#!/usr/bin/python3
"""Unittest for BaseModel class."""

import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test BaseModel."""

    def test_instance(self):
        """Test that BaseModel creates an instance."""
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)

    def test_id(self):
        """Test that BaseModel has an id."""
        my_model = BaseModel()
        self.assertIsNotNone(my_model.id)


if __name__ == "__main__":
    unittest.main()