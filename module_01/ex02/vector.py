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
        # Check if two
            # check is list
                # check is list of list
                    # check each list of list is float

        # Check if one
        # check if list of float
        if not vec:
            raise ValueError("Vector cannot be empty")
        if isinstance(vec, list) and all(isinstance(val, float) for val in vec):
            return vec
        raise ValueError("Vector must be list of floats or list of lists of floats")
        # raise error


#    @property
#    def get(self):
