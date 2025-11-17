import numpy as np
import numpy.linalg as linalg

class LogicApp:
    def __init__(self):
        # List of numpy vectors
        self.vectors = []
        # List of numpy matrices
        self.matrices = []

    def add_vector(self, v):
        if not isinstance(v, np.ndarray):
            raise TypeError("not a vector")
        self.vectors.append(v)

    def add_matrix(self, A):
        if not isinstance(A, np.ndarray):
            raise TypeError("not a matrix")
        self.matrices.append(A)

    def print_vectors(self):
        for i in range(len(self.vectors)):
            print(f"[{i}] ", self.vectors[i])

    def print_matrices(self):
        for i in range(len(self.matrices)):
            print(f"[{i}] ", self.matrices[i])

    def v_add(self, i, j):
        if self.vectors[i].shape[0] != self.vectors[j].shape[0]:
            raise TypeError("Vectors are not the same length")
        try:
            return self.vectors[i] + self.vectors[j]
        except Exception as e:
            return "Error", e
        
    def v_sub(self, i, j):
        if self.vectors[i].shape[0] != self.vectors[j].shape[0]:
            raise TypeError("Vectors are not the same length")
        try:
            return self.vectors[i] - self.vectors[j]
        except Exception as e:
            return "Error", e

    def v_smul(self, a, i): # scalar multiplication
        try:
            return a * self.vectors[i]
        except Exception as e:
            return "error", e
        
    def m_add(self, i, j):
        try:
            return self.matrices[i] + self.matrices[j]
        except Exception as e:
            return "error", e

    def m_sub(self, i, j):
        if self.vectors[i].shape[0] != self.vectors[j].shape[0]:
            raise TypeError("Vectors are not the same length")
        try:
            return self.matrices[i] - self.matrices[j]
        except Exception as e:
            return "Error", e

    def m_smul(self, a, i): # scalar matrix multiplication
        try:
            return a * self.matrices[i]
        except Exception as e:
            return "error", e

    def solve(self, A, x, b):
        if self.matrices[A].shape[1] != self.vectors[b].shape[0]:
            raise TypeError("matrix and vector size don't match")
        try:
            x = np.linalg.solve(A, b)
            return x
        except Exception as e:
            return "error", e

    def transpose(self, i):
        try:
            return self.vectors[i].T
        except Exception as e:
            return "error", e

    def matmul(self, i, j): # Matrix Multiplication
        if self.matrices[i].shape[1] != self.matrices[j].shape[2]:
            raise TypeError("Matrices do not match size")
        try:
            return self.matrices[i] @ self.matrices[j]
        except Exception as e:
            return "error", e

    def invert(self, i):
        if linalg.matrix_rank(self.vectors[i]) < self.vectors[i].shape[0]:
            raise TypeError("matrix is singular")
        try:
            return linalg.inv(self.vectors[i])
        except Exception as e:
            return "error", e

    def eigen(self, i): # returns (eigenvalues, eigenvectors)
        try:
            return linalg.eig(self.vectors[i])
        except Exception as e:
            return "error", e

    def dot(self, i, j):
        if len(self.vectors[i] != self.vectors[j]):
            raise TypeError("Vectors are not the same length")
        try:
            return np.dot(self.vectors[i], self.vectors[j])
        except Exception as e:
            return "error", e

    def det(self, i):
        try:
            return linalg.det(self.matrices[i])
        except Exception as e:
            return "error", e

    


        
