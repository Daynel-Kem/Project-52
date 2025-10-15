import numpy as np
import numbers

class Vector:
    def __init__(self, values):
        self.values = values

    def __add__(self, other):
        sum = []
        for i in range(self.size()):
            sum.append(self.values[i] + other.values[i])
        return sum 
    
    def __mul__(self, other):
        # Detects if other is a vector (Vector Multiplication)
        if (type(other) == '__main__.Vector'):
            pass

        # Detects if other is a number (Scalar Multiplication)
        elif (isinstance(other, numbers.Number)):
            product = []
            for i in range(self.size()):
                product.append(self.values[i] * other)
            return product

    # Applies the Euclidean Norm
    def norm(self):
        sum = 0
        for i in self.values:
            sum += i * i
        return np.sqrt(sum)
    
    # Returns the unit vector
    def unit(self):
        norm = 1 / self.norm()
        return self * norm

    def size(self):
        return len(self.values)
    
