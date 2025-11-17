from logic import LogicApp
import numpy as np

app = LogicApp()

v = np.array([3, 6, 1, 2])
u = np.array([6, 1, 2, 2])

A = np.array([[1, 2],
             [4, 6]])

app.add_vector(v)
app.add_vector(u)
# app.add_matrix(A)

# app.print_matrices()
app.print_vectors()

y = app.add(0, 1)
print(y)

print(app.smul(3, 0))