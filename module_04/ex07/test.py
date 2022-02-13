#!/usr/bin/env python3

from FileLoader import FileLoader
from MyPlotLib import MyPlotLib

if __name__ == "__main__":
    loader = FileLoader()
    data = loader.load('athlete_events.csv')
    mpl = MyPlotLib()
    mpl.histogram(data, ["Height", "Weight"])
    mpl.density(data, ["Weight", "Height"])
    mpl.pair_plot(data, ["Weight", "Height"])
    mpl.box_plot(data, ["Weight", "Height"])
