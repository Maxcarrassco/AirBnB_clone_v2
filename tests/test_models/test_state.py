#!/usr/bin/python3
""" """
import unittest
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """ """
    @unittest.skip('Skipping check for test name of state')
    def test_name3(self):
        """ """
        state = State()
        self.assertEqual(type(state.name), str)
