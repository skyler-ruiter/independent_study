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
      
  # solve for x using back substitution
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
  error = np.linalg.norm(x - np.array([1,1]))
  print("epsilon = %e,\tx = %s,\terror = %e" % (eps, x, error))
  
# part b

for eps in epsilons:
  A = np.array([[eps, 1], [1, 1]])
  b = np.array([1+eps, 2])
  x = gaussian_nopivot(A, b)
  r = b - (A @ x)
  x = x + gaussian_nopivot(A, r)
  error = np.linalg.norm(x - np.array([1,1]))
  print("epsilon = %e,\tx = %s,\terror = %e" % (eps, x, error))
  

"""
Output:
epsilon = 1.000000e-02, x = [1. 1.],                    error = 8.881784e-16
epsilon = 1.000000e-04, x = [1. 1.],                    error = 1.101341e-13
epsilon = 1.000000e-06, x = [1. 1.],                    error = 2.875566e-11
epsilon = 1.000000e-08, x = [0.99999999 1.        ],    error = 6.077471e-09
epsilon = 1.000000e-10, x = [1.00000008 1.        ],    error = 8.274037e-08
epsilon = 1.000000e-12, x = [0.99986686 1.        ],    error = 1.331440e-04
epsilon = 1.000000e-14, x = [0.99920072 1.        ],    error = 7.992778e-04
epsilon = 1.000000e-16, x = [2.22044605 1.        ],    error = 1.220446e+00
epsilon = 1.000000e-18, x = [0. 1.],                    error = 1.000000e+00
epsilon = 1.000000e-20, x = [0. 1.],                    error = 1.000000e+00

epsilon = 1.000000e-02, x = [0.49748744 1.00502513],    error = 5.025377e-01
epsilon = 1.000000e-04, x = [0.499975 1.00005 ],        error = 5.000250e-01
epsilon = 1.000000e-06, x = [0.49999975 1.0000005 ],    error = 5.000002e-01
epsilon = 1.000000e-08, x = [0.49999999 1.        ],    error = 5.000000e-01
epsilon = 1.000000e-10, x = [0.50000008 1.        ],    error = 4.999999e-01
epsilon = 1.000000e-12, x = [0.49998893 1.        ],    error = 5.000111e-01
epsilon = 1.000000e-14, x = [0.49920072 1.        ],    error = 5.007993e-01
epsilon = 1.000000e-16, x = [1.22044605 1.        ],    error = 2.204460e-01
epsilon = 1.000000e-18, x = [0. 1.],                    error = 1.000000e+00
epsilon = 1.000000e-20, x = [0. 1.],                    error = 1.000000e+00


The accuracy of the computed solution decreases as epsilon decreases.
it also doesn't seem that iterative refinement helps much in this case.

"""