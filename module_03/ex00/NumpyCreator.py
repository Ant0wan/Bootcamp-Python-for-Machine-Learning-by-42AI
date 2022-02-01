# pylint: disable=invalid-name
"""
ex00
"""

import numpy as np


# pylint: disable=no-self-argument
class NumPyCreator:
    """NumPyCreator"""

    def from_list(lst):
        """Takes a list or nested list and returns its
           corresponding Numpy array
        """
        return np.array(lst)

    def from_tuple(tpl):
        """Takes a tuple or nested tuple and returns
           its corresponding Numpy array
        """
        return np.array(tpl)

    def from_iterable(itr):
        """Takes an iterable and returns an array which
           contains all of its elements
        """
        return np.array(itr)

    def from_shape(shape, value=0):
        """Returns an array filled with the same value,
           The first argument is a tuple which specifies
           the shape of the array, the second argument
           specifies the value of all the elements.
           This value must be 0 by default
        """
        return np.full(shape, value)

    def random(shape):
        """Returns an array filled with random values,
           It takes as an argument a tuple which specifies
           the shape of the array
        """
        return np.random.random(shape)

    def identity(n):
        """Returns an array representing the identity
           matrix of size n
        """
        return np.identity(n)
