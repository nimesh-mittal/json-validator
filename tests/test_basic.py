from core.schema import Schema
from core.prop import Prop
from json_validator import validate_schema, validate_v1
import os
import unittest


class TestBasic(unittest.TestCase):

    def person_schema(self):
        prop = {
            "name": Prop().string().max(255).min(3).build(),
            "age": Prop().number().max(120).min(2).build()
        }

        return Schema().keys(prop).required(["name"]).build()

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test0(self):
        error = validate_v1({}, self.person_schema())
        self.assertEqual(error, ["'name' is a required property"])

    def test1(self):
        error = validate_v1({'name': 1}, self.person_schema())
        self.assertEqual(error, ["1 is not of type 'string'"])

    def test2(self):
        error = validate_v1({'name': '2x'}, self.person_schema())
        self.assertEqual(error, ["'2x' is too short"])

    def test3(self):
        error = validate_v1({'name': 'raj', 'age': '1'}, self.person_schema())
        self.assertEqual(error, ["'1' is not of type 'number'"])

    def test5(self):
        error = validate_v1({'age': '1'}, self.person_schema())
        self.assertEqual(error, ["'1' is not of type 'number'", "'name' is a required property"])

    def test6(self):
        error = validate_v1({'name': 'raj', 'age': 1}, self.person_schema())
        self.assertEqual(error, ['1 is less than the minimum of 2'])

    def test7(self):
        error = validate_v1({'name': 'raj', 'age': 150}, self.person_schema())
        self.assertEqual(error, ['150 is greater than the maximum of 120'])

if __name__ == '__main__':
    unittest.main()