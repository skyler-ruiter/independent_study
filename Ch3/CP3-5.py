"""
A planet follows an elliptical orbit, which can be represented in a 
Cartesian (x; y) coordinate system by the equation:

ay^2 + bxy + cx + dy + e = x^2


(a) Use a library routine, or one of your own design, for linear least 
squares to determine the orbital parameters a, b, c, d, e, given the 
following observations of the planet's position:

x | 1:02 0:95 0:87 0:77 0:67
y | 0:39 0:32 0:27 0:22 0:18
--|--------------------------
x | 0:56 0:44 0:30 0:16 0:01
y | 0:15 0:13 0:12 0:13 0:15

In addition to printing the values for the orbital parameters, plot 
the resulting orbit and the given data points in the (x; y) plane.


(b)This least squares problem is nearly rankdecient. To see what effect
this has on the solution, perturb the input data slightly by adding
to each coordinate of each data point a random number uniformly distributed 
on the interval [-0:005; 0:005] (see Section 13.5) and solve the least 
squares problem with the perturbed data. Compare the new values for the 
parameters with those previously computed. What effect does this difference 
have on the plot of the orbit? Can you explain this behavior?


(c) Solve the same least squares problem again, for both the original and 
the perturbed data, this time using a library routine (or one of your own 
design) speciffcally designed to deal with rank deffciency (by using 
column pivoting, for example). Such a routine usually includes as an input 
parameter a tolerance to be used in determining the numerical rank of the 
matrix. Experiment with various values for the tolerance, say,
10^-k, k = 1; : : : ; 5. What is the resulting rank of the matrix for each 
value of the tolerance? Compare the behavior of the two solutions (for the 
original and the perturbed data) with each other as the tolerance and the 
resulting rank change. How well do the resulting orbits fit the data points 
as the tolerance and rank vary? Which solution would you regard as better: 
one that fits the data more closely, or one that is less sensitive to small 
perturbations in the data? Why?


(d) Use a library routine to compute the singular value decomposition of the 
10x5 least squares matrix.


(e) Use the singular value decomposition to compute the solution to the least 
squares problem. With the singular values in order of decreasing magnitude, 
compute the solutions using the first k singular values, k = 1; : : : ; 5. 
For each of the five solutions obtained, print the values for the orbital 
parameters and also plot the resulting orbits along with the given data points 
in the (x; y) plane.


(f) Perturb the input data slightly by adding to each coordinate of each 
data point a random number uniformly distributed on the interval 
[-0:005; 0:005] (see Section 13.5). Compute the singular value decomposition 
of the new least squares matrix, and solve the least squares problem with 
the perturbed data as in part e. Compare the new values for the parameters 
with those previously computed for each value of k. What effect does this 
difference have on the plot of the orbits? Can you explain this behavior? 
Which solution would you regard as better: one that fits the data more 
closely, or one that is less sensitive to small perturbations in the data? Why?


(g) For simplicity, we have used ordinary least squares in this problem, 
but in fact all of the data are equally subject to observational errors 
(indeed, x appears on both sides of the equation), which makes the 
applicability of ordinary least squares questionable. Reformulate this 
problem as a total least squares problem and solve the latter using the 
singular value decomposition as described in Section 3.6.1.

"""