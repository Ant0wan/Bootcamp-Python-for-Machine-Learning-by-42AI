"""
Vectors
"""


class Vector:
    """Vector Class"""

    def __init__(self, vector=[]):
        self.__vector = list(vector)

    @staticmethod
    def _check_vector(vector):
        if isinstance(vector, list) and (all(isinstance(value, float) for value in vector) or all(isinstance(value, list) for value in vector)):


#    @property
#    def get(self):
