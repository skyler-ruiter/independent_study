"""
Suppose you need to generate n+1 equally spaced points on the interval
[a,b], with spacing h = (b-a)/n.

(a) In floating-point arithmetic, which of the following methods:
    x_0 = a,  x_k = x_(k-1) + h,    k = 1, ..., n
or
    x_k = a + kh,   k = 0, ..., n
is better, and why?

(b) Write a program implementing both methods nd find an example, 
say, with a = 0 and b = 1, that illustrates the difference between them.
"""

import numpy as np

a = 0
b = 1
n = 100
h = (b-a)/n

v1 = []
v1.append(a)
for i in range(1, n+1):
  v1.append(v1[i-1] + h)

v2 = np.zeros(n+1)
for k in range(n+1):
  v2[k] = a + (h*k)

print(v1)
print(v2)

print(np.max(np.abs(v1-v2)))

"""
The second method is far better since its calcutating the value directly each time where the first
method keeps accumulating error by using the previous value. So if the previous value is wrong we
just keep pushing it along through the loop.
"""