class Vector:
    def __init__(self, values):
        self._shape = None
        self.values = values

    def __str__(self):
        return f"{self.values}"

    def __repr__(self):
        return f"{self.values}"

    @property
    def values(self):
        return self._values

    @values.setter
    def values(self, values):
        if not (isinstance(values, list) and all(isinstance(sublist, list) and all(isinstance(value, float) for value in sublist) for sublist in values)) \
        and not isinstance(values, int) \
        and not (isinstance(values, tuple) and all(isinstance(value, int) for value in values)):
            raise TypeError('''vector initialization is only possible in one \
of those ways:
- a list of a list containing floats (row) or a list of lists containing \
floats (column)
- an integer indicating the vector's size (as column by default)
- a tuple with two integers indicating a range of values for the vector''')
        if isinstance(values, int):
            if values <= 0:
                raise ValueError("a vector can't have negative or 0 size")
            else:
                self._values = list()
                for i in range(0, values):
                    self._values.append([float(i)])
        if isinstance(values, tuple):
            if values[0] > values[1]:
                raise ValueError("negative vector range not supported")
            elif values[0] == values[1]:
                self._values = list([float(values[0])])
            else:
                self._values = list()
                for i in range(0, values[1] - values[0]):
                    self._values.append([float(values[0] + i)])
        if isinstance(values, list):
            self._values = values
        if len(self._values) == 1:
            self._shape = tuple((1, len(self.values[0])))
        else:
            self._shape = tuple((len(self.values), 1))

    @property
    def shape(self):
        return self._shape

    def dot(self, vector2):
        if not isinstance(vector2, Vector):
            raise TypeError("vector must be of type Vector")
        elif not self.shape == vector2.shape:
            raise ValueError("both vectors must be of same shape")
        result = 0
        if self.shape[0] == 1:
            for i in range(0, self.shape[1]):
                result += self.values[0][i] * vector2.values[0][i]
        else:
            for i in range(0, self.shape[0]):
                result += self.values[i][0] * vector2.values[i][0]
        return result

    def T(self):
        transposed = list()
        if self.shape[0] == 1:
            for value in self.values[0]:
                transposed.append([value])
        else:
            transposed.append(list())
            for i in range(0, self.shape[0]):
                transposed[0].append(self.values[i][0])
        return Vector(transposed)

    def __add__(self, vector2):
        if not isinstance(vector2, Vector):
            raise TypeError("both vectors must be of type Vector")
        elif not self.shape == vector2.shape:
            raise ValueError("both vectors must be of same shape")
        result_vector = list()
        if self.shape[0] == 1:
            result_vector.append(list())
            for i in range(0, self.shape[1]):
                result_vector[0].append(self.values[0][i] + vector2.values[0][i])
        else:
            for i in range(0, self.shape[0]):
                result_vector.append([self.values[i][0] + vector2.values[i][0]])
        return Vector(result_vector)

    def __radd__(self, vector2):
        return (self + vector2)

    def __sub__(self, vector2):
        if not isinstance(vector2, Vector):
            raise TypeError("both vectors must be of type Vector")
        elif not self.shape == vector2.shape:
            raise ValueError("both vectors must be of same shape")
        result_vector = list()
        if self.shape[0] == 1:
            result_vector.append(list())
            for i in range(0, self.shape[1]):
                result_vector[0].append(self.values[0][i] - vector2.values[0][i])
        else:
            for i in range(0, self.shape[0]):
                result_vector.append([self.values[i][0] - vector2.values[i][0]])
        return Vector(result_vector)

    def __rsub__(self, vector2):
        if not isinstance(vector2, Vector):
            raise TypeError("both vectors must be of type Vector")
        elif not self.shape == vector2.shape:
            raise ValueError("both vectors must be of same shape")
        result_vector = list()
        if self.shape[0] == 1:
            result_vector.append(list())
            for i in range(0, self.shape[1]):
                result_vector[0].append(vector2[0][i] - self.values[0][i])
        else:
            for i in range(0, self.shape[0]):
                result_vector.append([vector2[i][0] - self.values[i][0]])
        return Vector(result_vector)

    def __truediv__(self, scalar):
        if isinstance(scalar, Vector):
            raise NotImplementedError("Division of vectors is not defined here.")
        if not isinstance(scalar, int) and not isinstance(scalar, float):
            raise TypeError("scalar must be a float or an integer")
        elif scalar == 0:
            raise ZeroDivisionError("division by zero")
        result_vector = list()
        if self.shape[0] == 1:
            result_vector.append(list())
            for value in self.values[0]:
                result_vector[0].append(value / scalar)
        else:
            for i in range(0, self.shape[0]):
                result_vector.append([self.values[i][0] / scalar])
        return Vector(result_vector)

    def __rtruediv__(self, scalar):
        raise NotImplementedError("Division of a scalar by a Vector is not defined here.")

    def __mul__(self, scalar):
        if isinstance(scalar, Vector):
            raise NotImplementedError("Multiplication of vectors not defined here.")
        if not isinstance(scalar, int) and not isinstance(scalar, float):
            raise TypeError("scalar must be a float or an integer")
        result_vector = list()
        if self.shape[0] == 1:
            result_vector.append(list())
            for value in self.values[0]:
                result_vector[0].append(value * scalar)
        else:
            for i in range(0, self.shape[0]):
                result_vector.append([self.values[i][0] * scalar])
        return Vector(result_vector)

    def __rmul__(self, scalar):
        return self * scalar
