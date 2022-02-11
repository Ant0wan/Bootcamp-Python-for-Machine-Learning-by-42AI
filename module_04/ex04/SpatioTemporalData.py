# pylint: disable=invalid-name
"""
ex04
"""

import pandas


class SpatioTemporalData:
    """SpatioTemporalData"""

    def __init__(self, data: pandas.DataFrame):
        self.df = data

    def when(self, location: str) -> list:
        """ years based on location """
        return self.df[self.df['City'] == location]['Year'].unique()

    def where(self, date: int) -> list:
        """ game location """
        # "ID","Name","Sex","Age","Height","Weight","Team","NOC","Games","Year","Season","City","Sport","Event","Medal"
        pass
