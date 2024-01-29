"""
2.8. Multiplying both sides of a linear system Ax = b by a nonsingular diagonal matrix D to 
obtain a new system DAx = Db simply rescales the rows of the system and in theory does not 
change the solution. Such scaling does affect the condition number of the matrix and the choice
of pivots in Gaussian elimination, however, so it may affect the accuracy of the solution in finite-
precision arithmetic. Note that scaling can introduce some rounding error in the matrix unless the
entries of D are powers of the base of the floating-point arithmetic system being used (why?).

Using a linear system with randomly chosen matrix A, and right-hand-side vector b chosen so that
the solution is known, experiment with various scaling matrices D to see what effect they have
on the condition number of the matrix DA and the solution given by a library routine for solv-
ing the linear system DAx = Db. Be sure to try some fairly skewed scalings, where the magni-
tudes of the diagonal entries of D vary widely (the purpose is to simulate a system with badly chosen
units). Compare both the relative residuals and the error given by the various scalings. Can you
find a scaling that gives very poor accuracy? Is the residual still small in this case?
"""

import numpy as np
import matplotlib.pyplot as plt

norm = 2

# random matrix A
n = 10
A = np.random.rand(n,n)

# b
b = np.random.rand(n)
x = np.linalg.solve(A,b)

condition_nums = []
relat_resid = []
errors = []
i_vals = [i for i in range(20)]

for i in range(20):
  # make a diagonal matrix with increasingly bad scaling
  
  # diagonal matrix with 1's on the diagonal  
  D = np.eye(n)
  D[0,0] = 2**i
  
  x2 = np.linalg.solve(D@A,D@b)
  
  k = np.linalg.cond(D@A)
  
  r = np.linalg.norm(b-A@x)/(np.linalg.norm(A) * np.linalg.norm(x))
  
  e = np.linalg.norm(x-x2)/np.linalg.norm(x)
  
  print("The condition number of DA is", k)
  print("The relative residual is", r)
  print("The error is", e)
  print("=====================================")
  
  condition_nums.append(k)
  relat_resid.append(r)
  errors.append(e)


# log plot the condition numbers
plt.clf()
plt.semilogy(i_vals, condition_nums)
plt.xlabel("i")
plt.ylabel("Condition Number")
plt.title("Condition Number of DA")
plt.savefig("2-8_fig1.png")

# plot the relative residuals and errors log scale
plt.clf()
plt.semilogy(i_vals, relat_resid, label="Relative Residual")
plt.semilogy(i_vals, errors, label="Error")
plt.xlabel("i")
plt.ylabel("Relative Residual/Error")
plt.title("Relative Residual and Error of DA")
plt.legend()
plt.savefig("2-8_fig2.png")


# diagonal matrix with 1's on the diagonal  
D = np.eye(n)
D[0,0] = 2**20
D[3,3] = 2**-20
# D[5,5] = 2**40
# D[7,7] = 2
# D[8,8] = 1.99999

x2 = np.linalg.solve(D@A,D@b)

k = np.linalg.cond(D@A)

r = np.linalg.norm(b-A@x)/(np.linalg.norm(A) * np.linalg.norm(x))

e = np.linalg.norm(x-x2)/np.linalg.norm(x)

print("The condition number of DA is", k)
print("The relative residual is", r)
print("The error is", e)

"""
Skyler Notes:

The first part of the problem, asking why we need to use the power of the floating point system
is because we can represent the numbers in binary exactly with a base 2 system, but not with 
a base 10 system. So multipying by 2 is exact but multiplying by 10 is not.


The second part is to experiment with D to see what changes and to try and get a bad condiontion number.

- increasing the first diagonal entry of D to increasing powers of 2 it scales the condition number
  as seen in the frist plot with a straight line across the log scale

- the relative residual and error are both small for all values of i

- did not find a scaling that gives very poor accuracy but did find lots of bad condition numbers

"""
