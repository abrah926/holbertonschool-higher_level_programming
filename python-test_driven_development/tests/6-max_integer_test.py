#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function"""

    def test_positive_integers(self):
        """Test with positive integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_negative_integers(self):
        """Test with negative integers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-4, -3, -2, -1]), -1)

    def test_mixed_integers(self):
        """Test with a mix of positive and negative integers"""
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)
        self.assertEqual(max_integer([0, -2, -3, -1]), 0)

    def test_single_element(self):
        """Test with a single element"""
        self.assertEqual(max_integer([42]), 42)
        self.assertEqual(max_integer([-42]), -42)

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertIsNone(max_integer([]))

    def test_duplicate_max(self):
        """Test with duplicate maximum values"""
        self.assertEqual(max_integer([3, 3, 3, 3]), 3)

    def test_list_with_zeros(self):
        """Test with a list containing zeros"""
        self.assertEqual(max_integer([0, 0, 0, 0]), 0)

    def test_large_numbers(self):
        """Test with very large numbers"""
        self.assertEqual(max_integer([1000000, 999999, 123456789]), 123456789)

    def test_floats(self):
        """Test with a list of floats"""
        self.assertEqual(max_integer([1.1, 2.2, 3.3, 4.4]), 4.4)

    def test_mixed_floats_and_integers(self):
        """Test with a mix of floats and integers"""
        self.assertEqual(max_integer([1, 2.2, 3, 4.4]), 4.4)


if __name__ == "__main__":
    unittest.main()
