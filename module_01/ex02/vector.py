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
            elif all(isinstance(column, list) for column in vec):
                column_len = len(vec[0])
                for column in vec:
                    if not column:
                        raise ValueError("Vector cannot be empty")
                    if column_len != len(column):
                        raise ValueError("Value is not a correct vector")
                    if not all(isinstance(val, float) for val in column):
                        raise ValueError("Vector must be list of floats")
                return vec
        raise ValueError("Vector must be list of floats or list of lists of floats")

#    @property
#    def get(self):
