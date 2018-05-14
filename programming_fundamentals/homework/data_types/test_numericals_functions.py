#!/usr/bin/env python
"""
This module describes unittests for `numerical_functions` module.
This is needed for results verification only.
This is a helpful tool for mentors to verify the results of the students' home tasks.
"""
import unittest

from numericals_functions import (
    binary_to_decimal,
    decimal_to_binary)

__author__ = "Pavlo Ivanchyshyn"
__maintainer__ = "Pavlo Ivanchyshyn"
__email__ = "p.ivanchyshyn@gmail.com"


class TestNumericalFunctions(unittest.TestCase):

    def test_verify_result_type(self, fn, value, expected):

        message = "`{}` type is expected, but `{}` found."
        result = fn(value)
        assert type(result) == expected
        print(message.format(type(expected.__name__), type(result).__name__))

    def test_verify_results(self, fn, value, expected):
        message1 = "Decimal representation for `{}` value is `{}`, but `{}` found."
        message2 = "Binary representation for `{}` value is `{}`, but `{}` found."
        if value is not None:
            result = fn(value)
        else:
            result = fn()
        if fn == "binary_to_decimal":
            assert result == expected
            print(message1.format(value, expected, result))
        elif fn == "decimal_to_binary":
            assert result == expected
            print(message2.format(value, expected, result))

    def test_binary_to_decimal_values(self):

        TestNumericalFunctions.test_verify_results(self, binary_to_decimal, 10, 2)
        TestNumericalFunctions.test_verify_results(self, binary_to_decimal, 11010, 26)
        TestNumericalFunctions.test_verify_results(self, binary_to_decimal, 11010101010, 1706)

    def test_binary_to_decimal_result_type(self):
        self.test_verify_result_type(binary_to_decimal, 10, int)

    def test_decimal_to_binary_result_type(self):
        self.test_verify_result_type(decimal_to_binary, 2, int)

    def test_decimal_to_binary_values(self):

        self.test_verify_results(decimal_to_binary, 2, 10)
        self.test_verify_results(decimal_to_binary, 3, 11)
        self.test_verify_results(decimal_to_binary, 1990, 11111000110)
        self.test_verify_results(decimal_to_binary, 2018, 11111100010)

    def test_storage_result_type(self):
        self.test_verify_result_type(storage, [], list)
        self.test_verify_result_type(storage, ["message"], list)

    def test_storage_values(self):
        message = "Expected storage for `{}` value is `{}`, but `{}` found."

        self.test_verify_results(storage, [], ["data"], message)
        self.test_verify_results(storage, None, ["data"], message)
        self.test_verify_results(storage, ["test"], ["test", "data"], message)
        self.test_verify_results(storage, ["message"], ["message", "data"], message)

    def test_handle_exceptions_type(self):
        self.test_verify_result_type(handle_exceptions, 16, str)
        self.test_verify_result_type(handle_exceptions,, 100, str)
        self.test_verify_result_type(handle_exceptions,, '4', str)
        self.test_verify_result_type(handle_exceptions,, 'test', str)

    def test_handle_exceptions_values(self):
        message = "Expected message for `{}` value is `{}`, but `{}` found."

        self.verify_results(handle_exceptions, 1, "Wow! My number is lower.", message)
        self.verify_results(handle_exceptions, "1", "Wow! My number is lower.", message)
        self.verify_results(handle_exceptions, 41, "Wow! My number is lower.", message)
        self.verify_results(handle_exceptions, 42, "Wow! My number is lower.", message)
        self.verify_results(handle_exceptions, 43, "Yey! My number is higher!", message)
        self.verify_results(handle_exceptions, 1000, "Yey! My number is higher!", message)

if __name__ == '__main__':
    unittest.main()
