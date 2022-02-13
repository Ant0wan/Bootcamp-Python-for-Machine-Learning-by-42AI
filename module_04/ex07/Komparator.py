# pylint: disable=invalid-name
"""
ex07
"""

import pandas
import matplotlib.pyplot


class Komparator:
    """Komparator class"""
    def __init__(self, data):
        self.data = pandas.DataFrame

    def compare_box_plots(self, categorical_var, numerical_var):
        """displays a box plot with several boxes to
        compare how the distribution of the numerical
        variable changes if we only consider the subpopulation
        which belongs to each category
        """

    def density(self, categorical_var, numerical_var):
        """displays the density of the numerical variable"""
        pandas.DataFrame(data[features]).plot(kind='density')
        matplotlib.pyplot.show()

    def compare_histograms(self, categorical_var, numerical_var):
        """plots the numerical variable in a separate
        histogram for each category
        """
