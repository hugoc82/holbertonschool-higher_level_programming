#!/usr/bin/python3
"""Unittest for max_integer([..])"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test cases for the function max_integer"""
    
    def test_regular_case(self):
        """Test with a list of positive integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_positive_integers(self):
        """Test with another list of positive integers"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_negative_integers(self):
        """Test with a list of negative integers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_integers(self):
        """Test with a list of positive and negative integers"""
        self.assertEqual(max_integer([-1, 2, 3, -4]), 3)

    def test_single_element(self):
        """Test with a list of a single integer"""
        self.assertEqual(max_integer([5]), 5)

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertEqual(max_integer([]), None)

    def test_floats(self):
        """Test with a list of floats"""
        self.assertEqual(max_integer([1.1, 2.2, 3.3, 4.4]), 4.4)

    def test_mixed_integers_and_floats(self):
        """Test with a list of integers and floats"""
        self.assertEqual(max_integer([1, 2.2, 3, 4.4]), 4.4)

    def test_strings(self):
        """Test with a list of strings (should raise a TypeError)"""
        with self.assertRaises(TypeError):
            max_integer(["a", "b", "c"])

if __name__ == '__main__':
    unittest.main()
