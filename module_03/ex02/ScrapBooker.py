# pylint: disable=invalid-name
"""
ex02
"""

import numpy


class ScrapBooker:
    """Slicing method on numpy arrays"""

    @staticmethod
    def crop(array, dim, position=(0, 0)):
        """
        Crops the image as a rectangle via dim arguments
        (being the new height and width of the image) from
        the coordinates given by position arguments.
        """
        try:
            return array[position[0]:position[0] + dim[0],
                    position[1]:position[1] + dim[1]]
        except (ValueError, TypeError, IndexError):
            return None

    @staticmethod
    def thin(array, n, axis):
        """
        Deletes every n-th line pixels along the specified axis
        (0: vertical, 1: horizontal)
        """
        try:
            return numpy.delete(array, slice(n-1, None, n), axis)
        except (ValueError, TypeError, IndexError):
            return None

    @staticmethod
    def juxtapose(array, n, axis):
        """
        Juxtaposes n copies of the image along the specified axis.
        """
        try:
            return numpy.tile(array, (n, 1) if axis else n)
        except (ValueError, TypeError, IndexError):
            return None

    @staticmethod
    def mosaic(array, dim):
        """
        Makes a grid with multiple copies of the array.
        The dim argument specifies the number of repetition
        along each dimensions.
        """
        pass
