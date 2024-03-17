"""

(a) Implement both the classical and modiffed Gram-Schmidt procedures and 
use each to generate an orthogonal matrix Q whose columns form an orthonormal 
basis for the column space of the Hilbert matrix H, with entries 
h_ij = 1/(i+j- 1), for n = 2. . . ., 12 (see Computer Problem 2.6). As a 
measure of the quality of the results (speciffcally, the potential loss of 
orthogonality), plot the quantity -log_10(|| I - Q^T Q ||), which can be 
interpreted as "digits of accuracy," for each method as a function of n. 
In addition, try applying the classical procedure twice (i.e., apply your 
classical Gram-Schmidt routine to its own output Q to obtain a new Q), and 
again plot the resulting departure from orthogonality. How do the three 
methods compare in speed, storage, and accuracy?


(b) Repeat the previous experiment, but this time use the Householder method, 
that is, use the explicitly computed orthogonal matrix Q resulting from 
Householder QR factorization of the Hilbert matrix. Note that if the routine 
you use for Householder QR factorization does not form Q explicitly, then 
you can obtain Q by multiplying the sequence of Householder transformations 
times a matrix that is initialized to the identity matrix I (see previous 
exercise). Again, plot the departure from orthogonality for this method and
compare it with that of the previous methods.


(c) Repeat the previous experiment, but this time use the SVD to obtain the 
orthonormal basis (see Section 3.6.1).


(d) Yet another way to compute an orthonormal basis is to use the normal 
equations. If we form the cross-product matrix and compute its Cholesky
factorization A^TA = LL^T , then we have:

I = L^-1(A^T A)L^-T
  = (A L^-T)^T (A L^-T)
  
which means that Q = AL^-T is orthogonal, and its column space is obviously 
the same as that of A. Repeat the previous experiment using Hilbert matrices 
again, this time using the Q obtained in this way from the normal equations 
(the required triangular solution may be a little tricky to compute,
depending on the software you use). Again, plot the resulting departure from 
orthogonality and compare it with that of the previous methods.


(e) Can you explain the relative quality of the results you obtained for the 
various methods used in these experiments?

"""

