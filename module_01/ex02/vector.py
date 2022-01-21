"""
Vectors
"""


class Vector:
    """Vector Class"""

    def __init__(self, vector=[]):
        self.__vector = _check_vector(vector)

    @staticmethod
    def _check_vector(vec):
        """Check only 1 and 2 dimensions vectors"""
        if not vec:
            raise ValueError("Vector cannot be empty")
        if isinstance(vec, list):
            if all(isinstance(val, float) for val in vec):
                return vec
            elif all(isinstance(row, list) for row in vec):
                for row in vec:
                    if all(isinstance(val, float) for val in row):
                        return vec
        raise ValueError("Vector must be list of floats or list of lists of floats")

#    @property
#    def get(self):
