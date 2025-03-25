#!/usr/bin/python3
import unittest
from 6-max_integer import max_integer  # Assure-toi que l'importation est correcte

class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function"""

    def test_max_integer(self):
        """Test for normal cases"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)  # Liste avec des entiers
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)  # Liste avec des entiers
        self.assertEqual(max_integer([100, 50, 75]), 100)  # Liste avec des entiers
        self.assertEqual(max_integer([0, 0, 0, 0]), 0)  # Liste avec des zéros
        self.assertEqual(max_integer([-1, -2, -3]), -1)  # Liste avec des entiers négatifs
        self.assertEqual(max_integer([0.5, 1.5, 0.75]), 1.5)  # Liste avec des flottants

    def test_empty_list(self):
        """Test for an empty list"""
        self.assertIsNone(max_integer([]))  # Liste vide doit retourner None

    def test_single_element(self):
        """Test for a list with one element"""
        self.assertEqual(max_integer([10]), 10)  # Liste avec un seul élément

    def test_strings(self):
        """Test for a list of strings (should raise TypeError)"""
        with self.assertRaises(TypeError):
            max_integer(["a", "b", "c"])  # Liste de chaînes de caractères

    def test_mixed_types(self):
        """Test for a list with mixed types (should raise TypeError)"""
        with self.assertRaises(TypeError):
            max_integer([1, 2, "3", 4])  # Liste avec un mix de types (int et str)

if __name__ == "__main__":
    unittest.main()
