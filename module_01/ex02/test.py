#!/usr/bin/env python3
"""
Unit tests
"""

import unittest

from vector import Vector

class TestVectorClass(unittest.TestCase):
    """Test Class for functions and constant from vector module"""

    def test_check_vector(self):
        # Dimension 1
#        invalid_vec = ['0.0']
#        self.assertRaises(ValueError, Vector._check_vector, invalid_vec)
#        invalid_vec = ['0']
#        self.assertRaises(ValueError, Vector._check_vector, invalid_vec)
#        invalid_vec = ()
#        self.assertRaises(ValueError, Vector._check_vector, invalid_vec)
#        invalid_vec = [()]
#        self.assertRaises(ValueError, Vector._check_vector, invalid_vec)
#        invalid_vec = [0]
#        self.assertRaises(ValueError, Vector._check_vector, invalid_vec)
#        invalid_vec = [0, 0, 0, 0, 0, 0, 0]
#        self.assertRaises(ValueError, Vector._check_vector, invalid_vec)
#        invalid_vec = ['1.2', '3.4']
#        self.assertRaises(ValueError, Vector._check_vector, invalid_vec)
#        invalid_vec = ['', '']
#        self.assertRaises(ValueError, Vector._check_vector, invalid_vec)
#        invalid_vec = []
#        self.assertRaises(ValueError, Vector._check_vector, invalid_vec)
#        valid_vec = [0.0]
#        self.assertEqual(Vector._check_vector(valid_vec), valid_vec)
#        valid_vec = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
#        self.assertEqual(Vector._check_vector(valid_vec), valid_vec)
#        valid_vec = [1.2, 3.4]
#        self.assertEqual(Vector._check_vector(valid_vec), valid_vec)
#        valid_vec = [0.0, 1.0, 2.0, 3.0]
#        self.assertEqual(Vector._check_vector(valid_vec), valid_vec)
        # Dimension 2
        #vector1 = [[]]
        #vector1 = [[], [], [], []]
        #vector1 = [[0]]
        #vector1 = [[0.0]]
        #vector1 = [[1.2]]
        #vector1 = [[0.0], [1.0], [2.0], [3.0]]
        #vector2 = [[0.0, 2.5], [1.0, 5.7], [2.0, 7.9], [3.0, 7.7]]
        #vector4 = [[0.0], [1.0], [2.0], [3.0]]
        #vector5 = [[0.0], [1.0], [2.0], [3.0]]
        #self.assertEqual(Vector._check_vector([[0.0], [1.0], [2.0], [3.0]]), [[0.0], [1.0], [2.0], [3.0]])
        # From subject
        valid_vec = [[0.0], [1.0], [2.0], [3.0]]
        self.assertEqual(Vector._check_vector(valid_vec), valid_vec)
        valid_vec = [[0.0, 0.1], [1.0, 1.1], [2.0, 2.1], [3.0, 3.1]]
        self.assertEqual(Vector._check_vector(valid_vec), valid_vec)
        invalid_vec = [[0.0, 0.1], [1.0, 1.1], [2.0], [3.0, 3.1]]
        self.assertRaises(ValueError, Vector._check_vector, invalid_vec)
      #  invalid_vec = [[[0.0]], [[1.0]], [[2.0]], [[3.0]]]
      #  self.assertRaises(ValueError, Vector._check_vector, invalid_vec)
      #  invalid_vec = ([0.0], [1.0], [2.0], [3.0])
      #  self.assertRaises(ValueError, Vector._check_vector, invalid_vec)
      #  invalid_vec = [[0.0], [1.0], [2.0], [0]]
      #  self.assertRaises(ValueError, Vector._check_vector, invalid_vec)
      #  invalid_vec = [[[0.0], [1.0]], [[2.0], [3.0]]]
      #  self.assertRaises(ValueError, Vector._check_vector, invalid_vec)

   # def test_init(self):
   #     """Test vector constructor"""
   #     self.


if __name__ == '__main__':
    unittest.main(verbosity=2)
