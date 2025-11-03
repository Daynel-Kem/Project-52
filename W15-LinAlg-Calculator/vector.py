import numpy as np
import numbers

class Vector:
    def __init__(self, values):
        self.values = values
        self.size = len(values)

    def __add__(self, other):
        pass
    
    def __mul__(self, other):
        pass

    # Applies the Euclidean Norm
    def norm(self):
        pass
    
    # Returns the unit vector
    def unit(self):
        pass

    def size(self):
        return self.size
    
