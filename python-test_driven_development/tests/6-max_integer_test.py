#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
from 6-max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function."""

    def test_max_positive_integers(self):
        """Test with a list of positive integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_negative_integers(self):
        """Test with a list of negative integers."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_integers(self):
        """Test with a mix of positive and negative integers."""
        self.assertEqual(max_integer([-1, 2, 3, -4]), 3)

    def test_max_floats(self):
        """Test with a list of floating point numbers."""
        self.assertEqual(max_integer([1.5, 2.5, 3.5, 4.5]), 4.5)

    def test_mixed_floats_and_integers(self):
        """Test with a mix of floats and integers."""
        self.assertEqual(max_integer([1, 2.5, 3, 4.5]), 4.5)

    def test_empty_list(self):
        """Test with an empty list."""
        self.assertEqual(max_integer([]), None)

    def test_single_element(self):
        """Test with a list containing only one element."""
        self.assertEqual(max_integer([5]), 5)

    def test_strings(self):
        """Test with a list of strings (should raise TypeError)."""
        with self.assertRaises(TypeError):
            max_integer(["a", "b", "c"])

    def test_mixed_types(self):
        """Test with a list containing mixed types (should raise TypeError)."""
        with self.assertRaises(TypeError):
            max_integer([1, 2, "a", 4])

if __name__ == "__main__":
    unittest.main()
