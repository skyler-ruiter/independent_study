"""

Write a program implementing Lanczos iteration as given in 
Section 4.5.7. Test your program using a random real symmetric 
matrix A of order n having eigenvalues 1, 2, . . , n. To 
generate such a matrix, first generate an n x n matrix B with 
random entries uniformly distributed on the interval [0; 1) 
(see Section 13.5), and then compute the QR factorization 
B = QR. Now take A = Q D Q^T , where D = diag(1, . . ., n). The 
Lanczos algorithm generates only the tridiagonal matrix Tk at 
iteration k, so you will need to compute its eigenvalues (i.e., 
the Ritz values  i, i = 1, . . ., k) at each iteration, say, by 
using a library routine based on QR iteration. For the purpose 
of this exercise, run the Lanczos algorithm for a full n iterations.

To see graphically how the Ritz values behave as iterations proceed, 
construct a plot with the iteration number on the vertical axis and 
the Ritz values at each iteration on the horizontal axis. Plot each 
pair (i, k), i = 1, . . . , k, as a discrete point at each iteration 
k (see Fig. 4.4). As iterations proceed and the number of Ritz values 
grows correspondingly, you should see vertical "trails" of Ritz 
values converging on the true eigenvalues. Try several values for n, 
say, n = 10, 20, . . ., 50, making a separate plot for each.

"""