# pylint: disable=invalid-name
"""
ex01
"""

import numpy

from matplotlib import image
from matplotlib import pyplot


class ImageProcessor:
    """Load and display image as numpy array"""

    @staticmethod
    def load(path):
        """Load image from path as numpy array"""
        img = image.imread(path)
        array = numpy.array(img)
        shape = numpy.shape(array)
        print(f"Image dimensions: {shape[0]} x {shape[1]}")
        return array

    @staticmethod
    def display(array):
        """Display image from array"""
        pyplot.imshow(array)
        pyplot.axis("off")
        pyplot.show()
