import numpy as np
from fractions import Fraction
import sympy as sp

A=np.array([[0,5],
            [-1,6]])

A_inv = np.linalg.inv(A)

print(A_inv)

A=sp.Matrix([[0,5],
            [-1,6]])

A_invv = A.inv()
print(A_invv)

