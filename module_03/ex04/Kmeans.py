# pylint: disable=invalid-name
"""
ex04
input: python Kmeans.py filepath='../ressources/solar_system_census.csv' ncentroid=4 max_iter=30
"""

import argparse
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
        Args:
        -----
          X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Return:
        -------
          None.
        Raises:
        -------
          This function should not raise any Exception.
        """
        #... your code ...
        pass

    def predict(self, X):
        """
        Predict from wich cluster each datapoint belongs to.
        Args:
        -----
          X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Return:
        -------
          the prediction has a numpy.ndarray, a vector of dimension m * 1.
        Raises:
        -------
          This function should not raise any Exception.
        """
        #... your code ...
        pass


def main(*args):
    parser = argparse.ArgumentParser(prog='kmeans', description='Implementation of a basic Kmeans algorithm.')
    parser.add_argument('--version', action='version', version='%(prog)s 0.1')
    parser.add_argument('-f', '-filepath', '--filepath', nargs=1, type=argparse.FileType('r'), required=True)
    #parser.add_argument('-f', '-filepath', '--filepath', nargs=1, type=argparse.FileType('r'), default=sys.stdin)
    parser.add_argument('-n', '-ncentroid', '--ncentroid', nargs=1, type=int, required=True)
    parser.add_argument('-m', '-max_iter', '--max_iter', nargs=1, type=int, required=True)
    args = parser.parse_args()


if __name__ == '__main__':
    main()
