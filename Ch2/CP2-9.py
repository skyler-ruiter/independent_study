"""
2.9. (a) Use Gaussian elimination without piv-
oting to solve the linear system

[eps 1] [x1] = [1+eps]
[ 1  1] [x2] = [2    ]

for eps = 10^-2k, k = 1, . . . , 10. The exact solution
is x = [1 1], independent of the value of epsilon.
How does the accuracy of the computed solution
behave as the value of  decreases?

(b) Repeat part a, still using Gaussian elimination
without pivoting, but this time use one iteration of
iterative refinement to improve the solution, com-
puting the residual in the same precision as the
rest of the computations. Now how does the accu-
racy of the computed solution behave as the value
of epsilon decreases?
"""

import numpy as np

def gaussian_nopivot(A, b):
  n = len(b)
  
  for k in range(n-1):
    for i in range(k+1, n):
      aik = A[i,k]/A[k,k]
      for j in range(k+1, n):
        A[i,j] = A[i,j] - aik*A[k,j]
        
      b[i] = b[i] - aik*b[k]
      
  # solve for x
  x = np.zeros(n)
  x[n-1] = b[n-1]/A[n-1,n-1]
  for i in range(n-2, -1, -1):
    x[i] = (b[i] - np.dot(A[i,i+1:], x[i+1:]))/A[i,i]
  
  return x

# part a

epsilons = [10**(-2*k) for k in range(1,11)]

for eps in epsilons:
  A = np.array([[eps, 1], [1, 1]])
  b = np.array([1+eps, 2])
  x = gaussian_nopivot(A, b)
  print("epsilon = %e, x = %s" % (eps, x))
  
# part b

for eps in epsilons:
  A = np.array([[eps, 1], [1, 1]])
  b = np.array([1+eps, 2])
  x = gaussian_nopivot(A, b)
  r = b - (A @ x)
  x = x + gaussian_nopivot(A, r)
  print("epsilon = %e, x = %s" % (eps, x))