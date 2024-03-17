"""

Bioremediation involves the use of bacteria to consume toxic wastes. 
At steady state, the bacterial density x and nutrient concentration 
y satisfy the system of nonlinear equations:

  rxy - x(1 + y) = 0,
  -xy + (g - y)(1 + y) = 0,
  
where r and g are parameters that depend on various physical features 
of the system; typical values are r = 5 and g = 1. Solve this system 
numerically using Newton's method. You should find at least one solution 
with a nonzero bacterial density (x /= 0), and one solution in which 
the bacterial population has died out (x = 0).


"""