# pylint: disable=invalid-name
"""
ex00
"""

import numpy


# pylint: disable=no-self-use
class NumpyCreator:
    """NumPyCreator"""

    def from_list(self, lst):
        """Takes a list or nested list and returns its
           corresponding Numpy array
        """
        return numpy.array(lst)

    def from_tuple(self, tpl):
        """Takes a tuple or nested tuple and returns
           its corresponding Numpy array
        """
        return numpy.array(tpl)

    def from_iterable(self, itr):
        """Takes an iterable and returns an array which
           contains all of its elements
        """
        return numpy.array(itr)

    def from_shape(self, shape, value=0):
        """Returns an array filled with the same value,
           The first argument is a tuple which specifies
           the shape of the array, the second argument
           specifies the value of all the elements.
           This value must be 0 by default
        """
        return numpy.full(shape, value)

    def random(self, shape):
        """Returns an array filled with random values,
           It takes as an argument a tuple which specifies
           the shape of the array
        """
        return numpy.random.random(shape)

    def identity(self, n):
        """Returns an array representing the identity
           matrix of size n
        """
        return numpy.identity(n)
