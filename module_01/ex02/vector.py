"""
Vectors
"""


class Vector:
    """Vector Class"""

    def __init__(self, values):
        self.__values = self._define_vector(values)
        self.__shape = self.define_shape(self.__values)


    @staticmethod
    def _vector_from_size(size):
        vector = []
        for column in range(0, size):
            vector.extend([float(column)])
        return vector

    @staticmethod
    def _define_vector(vec):
        """Check only 1 and 2 dimensions vectors"""
        if not vec:
            raise ValueError("Vector cannot be empty")
        elif isinstance(vec, int):
            return Vector._vector_from_size(vec)
        elif isinstance(vec, tuple) and len(vec) == 2:
            if vec[0] < vec[1]:
                values = []
        elif isinstance(vec, list):
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

    @staticmethod
    def define_shape(vec):
        """Store dimension of the vector"""
        if isinstance(vec, list):
            if all(isinstance(val, float) for val in vec):
                return (len(vec), 1)
            elif all(isinstance(column, list) for column in vec):
                return (len(vec), len(vec[0]))

    @property
    def values(self):
        return self.__values

    @property
    def shape(self):
        return self.__shape
