"""

A Markov chain is a system that has n possible states and passes 
through a series of transitions from one state to another. The 
probability of a transition from state j to state i is given by a_ij, 
where 0 <= a_ij <= 1 and sum(i=1 to n) a_ij = 1. Let A denote the 
matrix of transition probabilities, and let (x_i)^(k) denote the 
probability that the system is in state i after transition k. If the 
initial probability distribution vector is x^(0), then the probability 
distribution vector after k steps is given by

x^(k) = Ax^(k-1) = A^k x^(0)

The long-term behavior of the system is therefore determined by the 
value of limit as k approaches infinity of A^k. Consider a system 
with three states and transition matrix:

    [ 0.8 0.2 0.1 ]
A = [ 0.1 0.7 0.3 ]
    [ 0.1 0.1 0.6 ]

and suppose that the system is initially in state 1.


(a) What is the probability distribution vector after three steps?


(b) What is the long-term value of the probability distribution vector?


(c) Does the long-term value of the probability distribution vector 
depend on the particular starting value x^(0)?


(d) What is the value of the limit as k approaches infinity of A^k,
and what is the rank of this matrix?


(e) Explain your previous results in the terms of the eigenvalues and
eigenvectors of the matrix A.


(f) Must 1 ALWAYS be an eigenvalue of the transition function of a Markov
chain? why?


(g) A probibility distribution vector x is said to be STATIONARY if 
Ax = x. How can you determine such a stationary value x using the 
eigenvalues and eigenvectors of A?


(h) How can you determine the stationary value x WITHOUT knowledge
of the eigenvalues and eigenvectors of A?


(i) In this particular example, is it possible for a previous distribution 
vector to recur, other than a stationary distribution? For Markov chains in 
general, is such nontrivial cyclic behavior possible? If not, why? If so, 
give an example. (Hint: Think about the location of the eigenvalues of A in 
the complex plane.)


(j) Can there be more than one stationary distribution vector for a given Markov 
chain? If not, why? If so, give an example.


(k) Of what numerical method does this problem remind you?

"""