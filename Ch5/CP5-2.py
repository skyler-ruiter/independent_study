"""

For the equation:

f(x) = x^2 - 3x + 2 = 0;

each of the following functions yields an equivalent
fixed-point problem:

  g_1(x) = (x^2 + 2)/3,
  g_2(x) = sqrt(3x - 2),
  g_3(x) = 3 - 2/x,
  g_4(x) = (x^2 - 2)/(2x - 3),
  
(a) Analyze the convergence properties of each of the corresponding 
fixed-point iteration schemes for the root x = 2 by considering |g'_i(2)|.


(b) Confirm your analysis by implementing each of the schemes and verifying 
its convergence (or lack thereof) and approximate convergence rate.

"""