"""
(a) Write a program to compute the approximate value for
the derivative of a function using the finite difference formula:

  f'(x) = (f(x+h) - f(x)) / h

Test your program using the function tan(x) for x=1. Determine the 
error by comparing with the square of the built-in function sec(x).
Plot h = 10^-k, k = 0, ..., 16. You should use log scale for h and
for the magnitude of the error. Is there a minimum value for the 
magnitude of the error? How does the corresponding value for h compare
with the rule of thumb h approx is sqrt(machine epsilon) derived in
example 1.3?

(b) Repeat the exercise using the centered difference approximation:

  f'(x) = (f(x+h) - f(x-h)) / 2h
"""

import math
import numpy as np
import matplotlib.pyplot as plt

def f(x):
  return math.tan(x)

def fp(x):
  return (1/math.cos(x))**2

def f_prime_forward(f, a, h):
  return (f((a + h)) - f(a)) / h

def f_prime_centered(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)

true = fp(1)
print(true)

guesses = []
error = []
h_values = np.logspace(-16, 0, 17)

for k in range(len(h_values)):
  guesses.append(f_prime_forward(f, 1, h_values[k]))
  error.append(abs(guesses[k] - true))

plt.loglog(h_values, error)
plt.xlabel("h (log scale)")
plt.ylabel("Error (log scale)")
plt.title("Error in forward difference approximation for tan(x) at x=1")
plt.grid(True)
plt.savefig('1-7_fig1.png')

guesses = []
error = []
h_values = np.logspace(-16, 0, 17)

for k in range(len(h_values)):
  guesses.append(f_prime_centered(f, 1, h_values[k]))
  error.append(abs(guesses[k] - true))
  
plt.clf()
plt.loglog(h_values, error)
plt.xlabel("h (log scale)")
plt.ylabel("Error (log scale)")
plt.title("Error in centered difference approximation for tan(x) at x=1")
plt.grid(True)
plt.savefig('1-7_fig2.png')


"""
The lowest point for both is ~10^-8 (centered difference is closer to 10^-7)
This relates to machine epsilon as shown in example 1.3 because its roughly equal to
the square root of our machine epsilon which we derived in 1.3 from an equation modeling
our total error from truncation and rounding error.
"""