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
            "gender": Prop().enum().values(['male', "female"]).build(),
        }

        return Schema().keys(prop).required(["name"]).build()

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test0(self):
        error = validate_v1({'name': "abc", "gender": 1}, self.person_schema())
        self.assertEqual(error, ["1 is not one of ['male', 'female']"])

    def test1(self):
        error = validate_v1({'name': "abc", "gender": 'unknown'}, self.person_schema())
        self.assertEqual(error, ["'unknown' is not one of ['male', 'female']"])

    def test4(self):
        error = validate_v1({'name': "abc", "gender": "male"}, self.person_schema())
        self.assertEqual(error, [])

if __name__ == '__main__':
    unittest.main()