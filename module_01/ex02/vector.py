"""
Vectors
"""


class Vector:
    """Vector Class"""

    def __init__(self, values):
        self.__values = self._define_vector(values)
        self.__shape = self._define_shape(self.__values)

    def __str__(self, spacing=' '):
        """Example:
            [[ 0  1  2  3  4]
             [ 5  6  7  8  9]
             [10 11 12 13 14]]
        """
        array = '['
        if all(isinstance(val, list) for val in self.__values):
            for column_index in range(0, self.__shape[0]):
                array += '['
                for row_index in range(0, self.__shape[1]):
                    array += f' {self.__values[column_index][row_index]}'
                if column_index == self.__shape[0] - 1:
                    array += ']'
                else:
                    array += ']\n' + spacing
        else:
            for row_index in range(0, self.__shape[1]):
                array += f'{self.__values[row_index]}'
                if row_index < self.__shape[1] - 1:
                    array += ' '
        array += ']'
        return array

    def __repr__(self):
        """Example:
            array([[ 0  1  2  3  4]
                   [ 5  6  7  8  9]
                   [10 11 12 13 14]])
        """
        return 'array(' + self.__str__('       ') + ')'

    def __add__(self, other):
        """Add two vectors of same dimension"""
        return self._iter_with(self, other, float.__add__)

    def __radd__(self, other):
        """Add two vectors of same dimension"""
        return Vector.__add__(other)

    def __sub__(self, other):
        """Substract two vectors of same dimension"""
        return self._iter_with(self, other, float.__sub__)

    def __rsub__(self, other):
        """Substract two vectors of same dimension"""
        return Vector.__sub__(other)

    def __truediv__(self, divisor):
        """Divide all vector member by divisor"""
        return self._iter_with(self, divisor, float.__truediv__)

    def __rtruediv__(self, divisor):
        """Divide all vector member by divisor"""
        return Vector.__truediv__(divisor)

    def __mul__(self, multiplier):
        """Multiply all vector member by multiplier"""
        return self._iter_with(self, multiplier, float.__mul__)

    def __rmul__(self, multiplier):
        """Multiply all vector member by multiplier"""
        return Vector.__mul__(multiplier)

    @staticmethod
    def _iter_with(self, other, func):
        """Apply func operator on all elements of a vector"""
        if isinstance(other, Vector) and self.__shape == other.shape:
            sum_values = self.__values
            if all(isinstance(val, list) for val in self.__values):
                for column_index in range(0, self.__shape[0]):
                    for row_index in range(0, self.__shape[1]):
                        sum_values[column_index][row_index] = func(sum_values[column_index][row_index], other.values[column_index][row_index])
            else:
                for row_index in range(0, self.__shape[1]):
                    sum_values[row_index] = func(sum_values[row_index], other.values[row_index])
            sum_vector = Vector(sum_values)
            return sum_vector
        elif isinstance(other, int) or isinstance(other, float):
            sum_values = self.__values
            if all(isinstance(val, list) for val in self.__values):
                for column_index in range(0, self.__shape[0]):
                    for row_index in range(0, self.__shape[1]):
                        sum_values[column_index][row_index] = func(sum_values[column_index][row_index], other)
            else:
                for row_index in range(0, self.__shape[1]):
                    sum_values[row_index] = func(sum_values[row_index], other)
            sum_vector = Vector(sum_values)
            return sum_vector
        raise ValueError("Can only add Vector types with same dimensions")


    @staticmethod
    def _vector_from_size(size):
        """Create vector made of size column with values from 0 to size"""
        return [[float(value)] for value in range(size)]

    @staticmethod
    def _vector_from_tuple(pair):
        """Create vector from tuple from [0] to [1]"""
        values = []
        if pair[0] == pair[1]:
            raise ValueError("Vector cannot be empty")
        elif pair[1] > pair[0]:
            for column in range(pair[0], pair[1]):
                values.append([float(column)])
        else:
            for column in range(pair[0], pair[1], -1):
                values.append([float(column - 1)])
        return values

    @staticmethod
    def _define_vector(vec):
        """Check only 1 and 2 dimensions vectors"""
        if not vec:
            raise ValueError("Vector cannot be empty")
        elif isinstance(vec, int):
            return Vector._vector_from_size(vec)
        elif isinstance(vec, tuple) and all(isinstance(val, int) for val in vec) and len(vec) == 2:
            return Vector._vector_from_tuple(vec)
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
    def _define_shape(vec):
        """Store dimension of the vector (row, column)"""
        if isinstance(vec, list):
            if all(isinstance(val, float) for val in vec):
                return (1, len(vec))
            elif all(isinstance(column, list) for column in vec):
                return (len(vec), len(vec[0]))

    @property
    def values(self):
        return self.__values

    @property
    def shape(self):
        return self.__shape

    @staticmethod
    def _arange(size):
        """Generate list of size elements != numpy.arange"""
        return [0.0] * size

    @staticmethod
    def _reshape(initial_array, row, column):
        """Change dimension of a list"""
        if len(initial_array) == row * column:
            array = []
            array_index = 0
            for ri in range(row):
                new_row = []
                for ci in range(column):
                    new_row.append(initial_array[array_index])
                    array_index += 1
                array.append(new_row)
            return array
        raise ValueError(f'cannot reshape array of size {len(initial_array)} into shape ({row},{column})')

    def dot(self, other):
        """Matrix product

         a.   0.0 3.0 5.0   b.  3.0         a[0][0]*b[0][0] + a[0][1]*b[1][0] + a[0][2]*b[2][0]
              5.0 5.0 2.0       4.0         a[1][0]*b[0][0] + a[1][1]*b[1][0] + a[1][2]*b[2][0]
                                3.0

         a.   0.0 3.0 5.0   b.  3.0 1.0     a[0][0]*b[0][0] + a[0][1]*b[1][0] + a[0][2]*b[2][0]   a[0][0]*b[0][1] + a[0][1]*b[1][1] + a[0][2]*b[2][1]
              5.0 5.0 2.0       4.0 2.0     a[1][0]*b[0][0] + a[1][1]*b[1][0] + a[1][2]*b[2][0]   a[1][0]*b[0][1] + a[1][1]*b[1][1] + a[1][2]*b[2][1]
                                3.0 3.0

        """
        """Results:

            27
            42

            27 21
            42 21

        """
        if not isinstance(other, Vector):
            raise TypeError('argurment must be of type Vector')
        if not isinstance(self.__values[0], list):
            self = Vector([self.__values])
        if not isinstance(other.values[0], list):
            other = Vector([other.values])
        if self.__shape[1] == other.shape[0]:
            scalar_product = self._reshape(self._arange(self.__shape[0] * other.shape[1]), self.__shape[0], other.shape[1])
            for b_column_index in range(other.shape[1]):
                for a_row_index in range(self.__shape[0]):
                    for a_column_index in range(self.shape[1]):
                        scalar_product[a_row_index][b_column_index] += self.__values[a_row_index][a_column_index] * other.values[a_column_index][b_column_index]
            return scalar_product
        raise ValueError(f"shapes ({self.__shape[0]},{self.__shape[1]}) and ({other.shape[0]},{other.shape[1]}) not aligned: {self.__shape[1]} (dim 1) != {other.shape[0]} (dim 0)")

    def T(self):
        """Transpose vector"""
        transpose = self._reshape(self._arange(self.__shape[0] * self.__shape[1]), self.__shape[1], self.__shape[0])
        if not isinstance(self.__values[0], list):
            self = Vector([self.__values])
        for col_index in range(self.__shape[0]):
            for row_index in range(self.__shape[1]):
                transpose[row_index][col_index] = self.__values[col_index][row_index]
        return Vector(transpose)
