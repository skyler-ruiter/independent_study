"""

The concentration of a drug in the bloodstream is expected to 
diminish exponentially with time. We will fit the model function:

y = f(t, x) = x_1 * e^(x_2 * t)

to the following data:

t | 0.5  1.0  1.5  2.0
y | 6.80 3.00 1.50 0.75
--|---------------------
t | 2.5  3.0  3.5  4.0
y | 0.48 0.25 0.20 0.15


(a) Perform the exponential fit using nonlinear least squares. 
You may use a library routine or one of your own design, perhaps 
using the Gauss- Newton method.


(b) Taking the logarithm of the model function gives 
log(x_1) + x_2 * t, which is now linear in x_2. Thus, an exponential 
fit can also be done using linear least squares, assuming that we 
also take logarithms of the data points y_i. Use linear least 
squares to compute x_1 and x_2 in this manner. Do the values obtained 
agree with those determined in part a? Why?

"""