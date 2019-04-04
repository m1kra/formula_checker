#!/usr/bin/python3

import unittest

from checker import are_parentheses_correct


class TestAreParenthesesCorrect(unittest.TestCase):
    def test_bad_order_of_braces(self):
        self.assertFalse(are_parentheses_correct(')('))
        self.assertFalse(
            are_parentheses_correct('(asdasd)sadasd{asdasd}Ads)(ads')
        )

    def test_missing_braces(self):
        self.assertFalse(are_parentheses_correct('('))
        self.assertFalse(
            are_parentheses_correct('y^{2-(3*u)} - [2*h - {4 - 5}')
        )

    def test_misaligned_braces(self):
        self.assertFalse(are_parentheses_correct('([)]'))
        self.assertFalse(are_parentheses_correct('{()}[{]}'))

    def test_empty_string(self):
        self.assertTrue(are_parentheses_correct(''))

    def test_string_without_braces(self):
        self.assertTrue(are_parentheses_correct('asdasd'))

    def test_only_braces(self):
        self.assertTrue(are_parentheses_correct('()'))
        self.assertTrue(are_parentheses_correct('[]'))
        self.assertTrue(are_parentheses_correct('{}'))

    def test_incorrect_mathematically(self):
        self.assertTrue(are_parentheses_correct('(1*+-/2)'))


if __name__ == '__main__':
    unittest.main()
