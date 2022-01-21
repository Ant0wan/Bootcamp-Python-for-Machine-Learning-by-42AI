#!/usr/bin/env python3
"""
Unit tests
"""

import unittest

from vector import Vector


class TestVectorClass(unittest.TestCase):
    """Test Class for functions and constant from vector module"""

    def test_check_vector_1D(self):
        """Test check_vector with vector of dimension 1"""
        invalid_vec = ['0.0']
        self.assertRaises(ValueError, Vector._check_vector, invalid_vec)
        invalid_vec = ['0']
        self.assertRaises(ValueError, Vector._check_vector, invalid_vec)
        invalid_vec = ()
        self.assertRaises(ValueError, Vector._check_vector, invalid_vec)
        invalid_vec = [()]
        self.assertRaises(ValueError, Vector._check_vector, invalid_vec)
        invalid_vec = [0]
        self.assertRaises(ValueError, Vector._check_vector, invalid_vec)
        invalid_vec = [0, 0, 0, 0, 0, 0, 0]
        self.assertRaises(ValueError, Vector._check_vector, invalid_vec)
        invalid_vec = ['1.2', '3.4']
        self.assertRaises(ValueError, Vector._check_vector, invalid_vec)
        invalid_vec = ['', '']
        self.assertRaises(ValueError, Vector._check_vector, invalid_vec)
        invalid_vec = []
        self.assertRaises(ValueError, Vector._check_vector, invalid_vec)
        valid_vec = [0.0]
        self.assertEqual(Vector._check_vector(valid_vec), valid_vec)
        valid_vec = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        self.assertEqual(Vector._check_vector(valid_vec), valid_vec)
        valid_vec = [1.2, 3.4]
        self.assertEqual(Vector._check_vector(valid_vec), valid_vec)
        valid_vec = [0.0, 1.0, 2.0, 3.0]
        self.assertEqual(Vector._check_vector(valid_vec), valid_vec)

    def test_check_vector_2D(self):
        """Test check_vector with vector of dimension 2"""
        invalid_vec = [[]]
        self.assertRaises(ValueError, Vector._check_vector, invalid_vec)
        invalid_vec = [[], [], [], []]
        self.assertRaises(ValueError, Vector._check_vector, invalid_vec)
        invalid_vec = [[0]]
        self.assertRaises(ValueError, Vector._check_vector, invalid_vec)
        valid_vec = [[0.0]]
        self.assertEqual(Vector._check_vector(valid_vec), valid_vec)
        valid_vec = [[1.2]]
        self.assertEqual(Vector._check_vector(valid_vec), valid_vec)
        valid_vec = [[0.0, 2.5], [1.0, 5.7], [2.0, 7.9], [3.0, 7.7]]
        self.assertEqual(Vector._check_vector(valid_vec), valid_vec)
        valid_vec = [[0.0, 2.5, 0.0, 0.0, 1.0, 5.7, 2.0, 7.9, 3.0, 7.7]]
        self.assertEqual(Vector._check_vector(valid_vec), valid_vec)
        valid_vec = [[0.0], [1.0], [2.0], [3.0]]
        self.assertEqual(Vector._check_vector(valid_vec), valid_vec)
        valid_vec = [[0.0, 0.1], [1.0, 1.1], [2.0, 2.1], [3.0, 3.1]]
        self.assertEqual(Vector._check_vector(valid_vec), valid_vec)
        invalid_vec = [[0.0, 0.1], [1.0, 1.1], [2.0], [3.0, 3.1]]
        self.assertRaises(ValueError, Vector._check_vector, invalid_vec)
        invalid_vec = [[0.5, 0.1], [1.0, 1.1], [2.0, 4.1], [3.0, 3]]
        self.assertRaises(ValueError, Vector._check_vector, invalid_vec)
        invalid_vec = [[[0.0, 0.0]], [[1.0, 1.0]], [[2.0, 2.0]], [[3.0, 3.0]]]
        self.assertRaises(ValueError, Vector._check_vector, invalid_vec)
        invalid_vec = ([0.0, 1.0], [1.0, 2.0], [2.0, 3.0], [3.0, 4.2])
        self.assertRaises(ValueError, Vector._check_vector, invalid_vec)
        invalid_vec = [[0.0], [1.0], [2.0], [0.321, 0.321]]
        self.assertRaises(ValueError, Vector._check_vector, invalid_vec)
        invalid_vec = [[], []]
        self.assertRaises(ValueError, Vector._check_vector, invalid_vec)
        invalid_vec = [[], [0.1]]
        self.assertRaises(ValueError, Vector._check_vector, invalid_vec)
        invalid_vec = [[1.0], []]
        self.assertRaises(ValueError, Vector._check_vector, invalid_vec)

    def test_check_vector_invalidD(self):
        """Test check_vector with vector of invalid dimension"""
        invalid_vec = [[[], []], [[], []]]
        self.assertRaises(ValueError, Vector._check_vector, invalid_vec)
        invalid_vec = [[[1.0], [1.0]], [[0.0], [0.0]]]
        self.assertRaises(ValueError, Vector._check_vector, invalid_vec)
        invalid_vec = [[[1.0, 1.0], [1.0, 0.0]], [[0.0, 4.5], [0.0, 4.5]]]
        self.assertRaises(ValueError, Vector._check_vector, invalid_vec)

    def test_init(self):
        """Test vector constructor"""
        with self.assertRaises(ValueError):
            invalid_vec = []
            Vector(invalid_vec)
        with self.assertRaises(ValueError):
            invalid_vec = [[[], []], [[], []]]
            Vector(invalid_vec)
        self.assertTrue(Vector([0.0, 1.0, 2.0, 3.0]))

    def test_values(self):
        """Test values method"""
        valid_vec = [0.0, 1.0, 2.0, 3.0]
        v1 = Vector(valid_vec)
        self.assertEqual(v1.values, valid_vec)
        valid_vec = [[0.0, 0.1], [1.0, 1.1], [2.0, 2.1], [3.0, 3.1]]
        v1 = Vector(valid_vec)
        self.assertEqual(v1.values, valid_vec)



if __name__ == '__main__':
    unittest.main(verbosity=2)
