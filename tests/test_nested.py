from core.schema import Schema
from core.prop import Prop
from json_validator import validate_schema, validate_v1
import os
import unittest


class TestBasic(unittest.TestCase):

    def person_schema(self):
        address_prop = {
            "line1": Prop().string().max(255).min(0).build(),
            "line2": Prop().string().max(255).min(0).build(),
            "pin": Prop().number().max(10).min(3).build(),
            "city": Prop().string().max(255).min(0).build(),
            "country": Prop().string().max(255).min(0).build()
        }

        prop = {
            "name": Prop().string().max(255).min(3).build(),
            "age": Prop().number().max(120).min(2).build(),
            "address": Prop().object().properties(address_prop).build(),
        }

        return Schema().keys(prop).required(["name"]).build()

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test0(self):
        error = validate_v1({'name': "abc", "address": 1}, self.person_schema())
        self.assertEqual(error, ["1 is not of type 'object'"])

    def test1(self):
        error = validate_v1({'name': "abc", "address": {'line1': 2}}, self.person_schema())
        self.assertEqual(error, ["2 is not of type 'string'"])

    def test3(self):
        error = validate_v1({'name': "abc", "address": {'line1': 2, 'country': None}}, self.person_schema())
        self.assertEqual(error, ["2 is not of type 'string'", "None is not of type 'string'"])

    def test4(self):
        error = validate_v1({'name': "abc", "address": {}}, self.person_schema())
        self.assertEqual(error, [])

if __name__ == '__main__':
    unittest.main()