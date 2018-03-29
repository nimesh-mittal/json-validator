from core.schema import Schema
from core.prop import Prop
from json_validator import validate_schema, validate_v1
import os
import unittest


class TestBasic(unittest.TestCase):

    def person_schema(self):
        prop = {
            "name": Prop().string().max(255).min(3).build(),
            "age": Prop().number().max(120).min(2).build(),
            "address": Prop().array().items({'type': 'string'}).max(2).min(1).build(),
        }

        return Schema().keys(prop).required(["name"]).build()

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test0(self):
        error = validate_v1({'name': "abc", 'address':1}, self.person_schema())
        self.assertEqual(error, ["1 is not of type 'array'"])

    def test1(self):
        error = validate_v1({'name': "abc", 'address':[]}, self.person_schema())
        self.assertEqual(error, ['[] is too short'])

    def test2(self):
        error = validate_v1({'name': "abc", 'address':[1,2]}, self.person_schema())
        self.assertEqual(error, ["1 is not of type 'string'", "2 is not of type 'string'"])

    def test3(self):
        error = validate_v1({'name': "abc", 'address':[1, True]}, self.person_schema())
        self.assertEqual(error, ["1 is not of type 'string'", "True is not of type 'string'"])

    def test4(self):
        error = validate_v1({'name': "abc", 'address':["a", "b", "c"]}, self.person_schema())
        self.assertEqual(error, ["['a', 'b', 'c'] is too long"])

    def test5(self):
        error = validate_v1({'name': "abc", 'address':["a", "b"]}, self.person_schema())
        self.assertEqual(error, [])

if __name__ == '__main__':
    unittest.main()