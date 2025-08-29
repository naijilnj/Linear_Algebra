import numpy as np
import sympy as sp

#A = sp.Matrix([[1, 1, 3],
#              [1, 5, 1],
#              [3, 1, 1]])

A = sp.Matrix([[5,4],
               [1,2]])

U = sp.Matrix([[1, 0, 0],
              [0, 1, 0],
              [0, 0, 1]])

x1 = sp.symbols("x1")
x2 = sp.symbols("x2")
#x3 = sp.symbols("x3")


x=sp.symbols(f"x1:{A.shape[0]+1}")
X=sp.Matrix(x)

Xt= sp.Matrix([[x1], 
               [x2]])

a = sp.symbols("a")

if A.shape[0] == A.shape[1]:
 print("Its a Square Matrix")
 K=(A-a*sp.eye(A.shape[0])).det()
 print("Characteristics Equation =",K)
 if K.coeff(a, 3)==-1 or K.coeff(a, 2)==-1:
   K=K*-1
   print(K)
 factored = sp.factor(K)
 print(factored)
 roots=sp.solve(factored)
 print("Eigen Values =",roots)
 J=(A-a*sp.eye(A.shape[0]))*X
 print("[A-LAMBDA*I]X = ",J)

 val1=0
 for i in roots:
    val1 = J.subs({a:i})
    print(val1)
    eq1=val1[0]
    eq2=val1[1]
    if A.shape[0]>=3:
     vars=list(sp.symbols(f"x1:{A.shape[0]+1}"))
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
     print(f"Eigen Vectors when {i} =",cross_n)
    else:
      vars=list(sp.symbols(f"x1:{A.shape[0]+1}"))
      coeff_eq1 = [eq1.coeff(v) for v in vars]
      v1=np.array(coeff_eq1)
      print("V1",v1)
#      for entry in v1:
#        if entry!=0:
#          divisor=entry
#      v11=v1 / divisor
#      print(v11)
      soln = sp.solve([eq1,eq2],[x1,x2])
      print(soln)
      coeffs = []
      for lhs, rhs in soln.items():
       coeffs.append(lhs.as_coefficients_dict().get(lhs, 0))   # coefficient of lhs variable
       for var in rhs.free_symbols:
        coeffs.append(rhs.as_coefficients_dict().get(var, 0))
      print(f"Eigen Vectors when {i} =",coeffs)
else:
  print("Its not a Square Matrix")



#      solnn = (soln.coeff(v) for v in vars)
#      print(solnn)