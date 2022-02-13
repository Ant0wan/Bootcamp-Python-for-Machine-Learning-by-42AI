# pylint: disable=invalid-name
"""
ex06
"""

import pandas


class MyPlotLib:
    """This class implements different plotting methods"""

#    def __init__(self, data: pandas.DataFrame, names: list):
#        self.data = data
#        self.names = names

    @staticmethod
    def histogram(data: pandas.DataFrame, features: list):
        """lots one histogram for each numerical feature in
        the list"""
        ax = data.plot.hist(bins=12, alpha=0.5)

    @staticmethod
    def density(data: pandas.DataFrame, features: list):
        """plots the density curve of each numerical feature in
        the list"""

    @staticmethod
    def pair_plot(data: pandas.DataFrame, features: list):
        """lots a matrix of subplots
        """

    @staticmethod
    def box_plot(data: pandas.DataFrame, features: list):
        """displays a box plot for each numerical
        variable in the dataset
        """
