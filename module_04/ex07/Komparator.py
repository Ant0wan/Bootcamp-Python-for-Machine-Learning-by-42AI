# pylint: disable=invalid-name
"""
ex07
"""

import pandas
import matplotlib.pyplot

from MyPlotLib import MyPlotLib

#"ID","Name","Sex","Age","Height","Weight","Team","NOC","Games","Year","Season","City","Sport","Event","Medal"


class Komparator:
    """Komparator class"""
    def __init__(self, data: pandas.DataFrame):
        self.data = data

    def compare_box_plots(self, categorical_var, numerical_var):
        """displays a box plot with several boxes to
        compare how the distribution of the numerical
        variable changes if we only consider the subpopulation
        which belongs to each category
        """
   #     plt = MyPlotLib()
   #     plt.box_plot(self.data, [categorical_var, numerical_var])


    def density(self, categorical_var, numerical_var):
        """displays the density of the numerical variable"""
        #pandas.DataFrame(data[features]).plot(kind='density')
        #matplotlib.pyplot.show()
#        mpl = MyPlotLib()
#        df = self.data
#        mpl.density(df, ["Sex", "Height"])

    def compare_histograms(self, categorical_var, numerical_var):
        """plots the numerical variable in a separate
        histogram for each category
        """
        categories = list(self.data[categorical_var].unique())
        ncat = len(categories)

        fig, axs = matplotlib.pyplot.subplots(ncols=ncat)

        for index, cat in enumerate(categories):
            mask = self.data[categorical_var] == cat
            axs[index].set_title(cat)
            axs[index].hist(self.data[mask][numerical_var].dropna())
            axs[index].grid()

        matplotlib.pyplot.show()
