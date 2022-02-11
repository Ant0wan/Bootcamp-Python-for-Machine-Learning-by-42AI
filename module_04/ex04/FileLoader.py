# pylint: disable=invalid-name
"""
ex01
"""

import os
import pandas


class FileLoader:
    """FileLoader class"""

    @staticmethod
    def load(path: os.path) -> pandas.DataFrame:
        """Take filepath and return panda data frame"""
        data = pandas.read_csv(path)
        # pylint: disable=no-member
        print(f"Loading dataset of dimensions \
{data.shape[0]} x {data.shape[1]}")
        return data

    @staticmethod
    def display(df, n):
        """Display data frame n first lines"""
        print(df.head(n))
