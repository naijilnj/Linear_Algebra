import numpy as np

A = np.array([[4, 1],
              [3, 2]])

x = np.linalg.det(A)
print(round(x))