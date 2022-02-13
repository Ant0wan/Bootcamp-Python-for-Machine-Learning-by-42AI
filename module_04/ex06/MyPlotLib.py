# pylint: disable=invalid-name
"""
ex06
"""

import pandas
import matplotlib.pyplot


class MyPlotLib:
    """This class implements different plotting methods"""
    @staticmethod
    def histogram(data: pandas.DataFrame, features: list):
        """lots one histogram for each numerical feature in
        the list"""
        nfeatures = len(features)
        # pylint: disable=unused-variable
        fig, axs = matplotlib.pyplot.subplots(ncols=nfeatures)
        for hist_index in range(nfeatures):
            axs[hist_index].set_title(features[hist_index])
            axs[hist_index].hist(data[features[hist_index]].dropna())
            axs[hist_index].grid()
        matplotlib.pyplot.show()

    @staticmethod
    def density(data: pandas.DataFrame, features: list):
        """plots the density curve of each numerical feature in
        the list"""
        pandas.DataFrame(data[features]).plot(kind='density')
        matplotlib.pyplot.show()

    @staticmethod
    def pair_plot(data: pandas.DataFrame, features: list):
        """lots a matrix of subplots"""
        pandas.plotting.scatter_matrix(data[features])
        matplotlib.pyplot.show()

    @staticmethod
    def box_plot(data: pandas.DataFrame, features: list):
        """displays a box plot for each numerical
        variable in the dataset
        """
        # pylint: disable=unused-variable
        fig, axs = matplotlib.pyplot.subplots()
        axs.boxplot(data[features].dropna(), labels=features)
        matplotlib.pyplot.show()
