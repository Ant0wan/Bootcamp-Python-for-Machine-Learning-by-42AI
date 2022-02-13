#!/usr/bin/env python3

from FileLoader import FileLoader
from MyPlotLib import MyPlotLib

if __name__ == "__main__":
    loader = FileLoader()
    data = loader.load('athlete_events.csv')
    myplot = MyPlotLib()
    myplot.histogram(data, ['Team'])
