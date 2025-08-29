import numpy as np

A = np.array([[2, 1], [1, -3]])
b = np.array([4, 1])


x=np.linalg.solve(A,b)
print(x)

#Addition
C=A+B
print(C)

#Scalar Multiplication
K=3*A
print(K)

#Dot Product
J=A@B
print("J",J)

#Transpose
A_t=A.T
print(A_t)

