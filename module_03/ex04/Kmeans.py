# pylint: disable=invalid-name
"""
ex04
input: python Kmeans.py filepath='../ressources/solar_system_census.csv' ncentroid=4 max_iter=30
tuto: https://www.youtube.com/watch?v=EItlUEPCIzM
"""

import argparse
import numpy
import sys


class KmeansClustering:
    def __init__(self, max_iter=20, ncentroid=5):
        self.ncentroid = ncentroid # number of centroids
        self.max_iter = max_iter # number of max iterations to update the centroids
        self.centroids = [] # values of the centroids

    def fit(self, X):
        """
        Run the K-means clustering algorithm.
        For the location of the initial centroids, random pick ncentroids from the dataset.
        """
        pass

    def predict(self, X):
        """
        Predict from wich cluster each datapoint belongs to.
        """
        pass


def main(*args):
    parser = argparse.ArgumentParser(prog='kmeans', description='Implementation of a basic Kmeans algorithm.')

    parser.add_argument('--version', action='version', version='%(prog)s 0.1')
    parser.add_argument('-f', '-filepath', '--filepath', nargs=1, type=argparse.FileType('r'), required=True)
    parser.add_argument('-n', '-ncentroid', '--ncentroid', nargs=1, type=int)
    parser.add_argument('-m', '-max_iter', '--max_iter', nargs=1, type=int)

    args = parser.parse_args()

    kmean = KmeansClustering(args.max_iter, args.ncentroid)
    kmean.fit()


if __name__ == '__main__':
    main()
