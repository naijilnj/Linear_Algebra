import numpy as np
import sympy as sp

#A = sp.Matrix([[1, 1, 3],
#              [1, 5, 1],
#              [3, 1, 1]])

A = sp.Matrix([[5, 4],
               [1, 2]])

U = sp.Matrix([[1, 0, 0],
              [0, 1, 0],
              [0, 0, 1]])

x1 = sp.symbols("x1")
x2 = sp.symbols("x2")
x3 = sp.symbols("x3")

X= sp.Matrix([[x1], 
              [x2],
              [x3]])
#eigenvalues, eigenvectors = np.linalg.eig(A)
#print(eigenvalues, eigenvectors)

a = sp.symbols("a")

if A.shape[0] == A.shape[1]:
 print("Its a Square Matrix")
 K=(A-a*sp.eye(A.shape[0])).det()
 print(K)
 if K.coeff(a, 3)==-1:
   K=K*-1
   print(K)
   factored = sp.factor(K)
   print(factored)
   roots=sp.solve(factored)
   print(roots)
   J=(A-a*sp.eye(A.shape[0]))*X
   print(J)
#   val=0
#   for i in roots:
#     val = J.subs({a:i})
#     print(val)
   val1=0
   for i in J:
    val1 = J.subs({a:roots[i]})
    print(val1)
    eq1=val1[0]
    eq2=val1[1]
    vars=[x1,x2,x3]
    coeff_eq1 = [eq1.coeff(v) for v in vars]
    coeff_eq2 = [eq2.coeff(v) for v in vars]
    v1=np.array(coeff_eq1)
    v2=np.array(coeff_eq2)
    cross = np.cross(v1,v2)
    print(cross)
    for entry in cross:
      if entry!=0:
        divisor=entry
        break
    cross_n=cross / divisor
    print(cross_n)
else:
  print("Its not a Square Matrix")