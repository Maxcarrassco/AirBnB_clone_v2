#!/usr/bin/python3
""" """
import unittest
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    @unittest.skip('Skipping test for city id')
    def test_state_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    @unittest.skip('Skipping test for city name')
    def test_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)
