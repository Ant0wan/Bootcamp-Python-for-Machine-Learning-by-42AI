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
        Args:
        -----
          array: numpy.ndarray
          dim: tuple of 2 integers.
          position: tuple of 2 integers.
        Return:
        -------
          new_arr: the cropped numpy.ndarray.
          None (if combinaison of parameters not compatible).
        Raise:
        ------
          This function should not raise any Exception.
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
        Args:
        -----
          array: numpy.ndarray.
          n: non null positive integer lower than the number of
          row/column of the array (depending of axis value).
          axis: positive non null integer.
        Return:
        -------
          new_arr: thined numpy.ndarray.
          None (if combinaison of parameters not compatible).
        Raise:
        ------
          This function should not raise any Exception.
        """
        try:
            print('ok')
        except (ValueError, TypeError, IndexError):
            return None

    @staticmethod
    def juxtapose(array, n, axis):
        """
        Juxtaposes n copies of the image along the specified axis.
        Args:
        -----
          array: numpy.ndarray.
          n: positive non null integer.
          axis: integer of value 0 or 1.
        Return:
        -------
          new_arr: juxtaposed numpy.ndarray.
          None (combinaison of parameters not compatible).
        Raises:
        -------
          This function should not raise any Exception.
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
        Args:
        -----
          array: numpy.ndarray.
          dim: tuple of 2 integers.
        Return:
        -------
          new_arr: mosaic numpy.ndarray.
          None (combinaison of parameters not compatible).
        Raises:
        -------
          This function should not raise any Exception.
        """
        pass
