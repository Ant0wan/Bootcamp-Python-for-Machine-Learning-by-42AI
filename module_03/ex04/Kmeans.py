# pylint: disable=invalid-name
"""
ex04
input: python Kmeans.py filepath='../ressources/solar_system_census.csv' ncentroid=4 max_iter=30
"""

from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans

import argparse
import itertools
import pandas
import numpy
import sys


class KmeansClustering:
    def __init__(self, max_iter=20, ncentroid=5):
        self.ncentroid = ncentroid # number of centroids
        self.max_iter = max_iter # number of max iterations to update the centroids
        self.centroids = [] # values of the centroids
        #self.headers = []
        #self.kmeans = None

    def fit(self, X: pandas.core.frame.DataFrame):
        """
        Run the K-means clustering algorithm.
        For the location of the initial centroids, random pick ncentroids from the dataset.
        """
        self.kmeans = KMeans(n_clusters=self.ncentroid, n_init=self.max_iter)
        self.headers = list(X.columns)
        self.kmeans.fit(X[self.headers])

    def predict(self, X: pandas.core.frame.DataFrame):
        """
        Predict from wich cluster each datapoint belongs to.
        """
        self.kmeans.predict(X)
        self.centroids = self.kmeans.cluster_centers_
        return self.centroids


def plot(points, km, ncentroid):
    """
    Plot clusters on 3D graph and display centroid info
    """
    fig = pyplot.figure()
    ax = fig.add_subplot(projection='3d')

    markers = iter(('o', 'v', 's', 'D', '+'))

    for centroid in range(ncentroid):
        mask = km.kmeans.labels_ == centroid
        print(sum(mask), 'elements in centroid', centroid, 'with coordinates', km.kmeans.cluster_centers_[centroid])
        ax.scatter(points[km.headers[0]][mask], points[km.headers[1]][mask], points[km.headers[2]][mask], marker=next(markers))

    ax.scatter(km.kmeans.cluster_centers_[:,0], km.kmeans.cluster_centers_[:,1], km.kmeans.cluster_centers_[:,2], c='r', marker='X')

    ax.set_xlabel(km.headers[0])
    ax.set_ylabel(km.headers[1])
    ax.set_zlabel(km.headers[2])

    pyplot.show()


def main():
    parser = argparse.ArgumentParser(prog='kmeans', description='Implementation of a basic Kmeans algorithm.')

    parser.add_argument('--version', action='version', version='%(prog)s 0.1')
    parser.add_argument('-f', '-filepath', '--filepath', type=str, required=True)
    parser.add_argument('-n', '-ncentroid', '--ncentroid', type=int)
    parser.add_argument('-m', '-max_iter', '--max_iter', type=int)

    args = parser.parse_args()

    # Get data and clean it from csv
    raw = pandas.read_csv(args.filepath)
    mask = raw.columns.str.match("Unnamed")
    points = raw.loc[:,~mask]

    # Kmeans clustering
    km = KmeansClustering(args.max_iter, args.ncentroid)
    km.fit(points)

    # Plot clusters
    plot(points, km, args.ncentroid)


if __name__ == '__main__':
    main()
