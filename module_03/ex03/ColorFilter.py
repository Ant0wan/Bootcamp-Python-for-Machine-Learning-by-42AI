# pylint: disable=invalid-name
"""
ex03
"""

import numpy


class ColorFilter:
    """Change color of picture through filters"""

    @staticmethod
    def invert(array):
        """Applies a blue filter to the image received as a numpy array."""
        return 1 - array

    @staticmethod
    def to_blue(array):
        """Applies a blue filter to the image received as a numpy array."""
        array[:, :, (0, 1)] = 0
        return array

    @staticmethod
    def to_green(array):
        """Applies a green filter to the image received as a numpy array."""
        return array * [0, 1, 0]

    @staticmethod
    def to_red(array):
        """Applies a red filter to the image received as a numpy array."""
        return array - ColorFilter.to_green(array) - ColorFilter.to_blue(array)

    @staticmethod
    def to_celluloid(array):
        """Applies a celluloid filter to the image received as a numpy array.
        Celluloid filter must display at least four thresholds of shades.
        Be careful! You are not asked to apply black contour on the object,
        you only have to work on the shades of your images.
        """
        return numpy.round(array)

    @staticmethod
    def to_grayscale(array, filter_, weights=None):
        """Applies a grayscale filter to the image received as a numpy array.
        For filter = ’mean’/’m’: performs the mean of RBG channels.
        For filter = ’weight’/’w’: performs a weighted mean of RBG channels
        """
        if filter_ in ('weighted', 'w'):
            return numpy.dot(array[..., :3], weights)
        mean = numpy.sum(array, axis=2) / 3
        return numpy.broadcast_to(mean[..., None], array.shape)
