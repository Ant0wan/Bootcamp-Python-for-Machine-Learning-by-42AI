#!/usr/bin/env python3
"""
Unit tests
"""

import unittest

from vector import Vector

class TestVectorClass(unittest.TestCase):
    """Test Class for functions and constant from vector module"""

    def test_check_vector(self):
        self.assertEqual(Vector._check_vector([1.2, 3.4]), [1.2, 3.4])
        self.assertEqual(Vector._check_vector([0.0, 1.0, 2.0, 3.0]), [0.0, 1.0, 2.0, 3.0])
        self.assertRaises(ValueError, Vector._check_vector, ['1.2', '3.4'])
        self.assertRaises(ValueError, Vector._check_vector, ['', ''])
        self.assertRaises(ValueError, Vector._check_vector, [])


   # def test_init(self):
   #     """Test vector constructor"""
   #     self.


if __name__ == '__main__':
    unittest.main(verbosity=2)
