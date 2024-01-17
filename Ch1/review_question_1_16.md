### Explain the distinction between computational error and propagated data error.

Computational error is the error propogated through the program by doing computations 
where propogated data error is the initial data coming in having error and propogating throgh the problem

A problem is said to be insensitive or well-conditioned if given relative change in the input data causes
a reasonable change in the solution. The opposite of this would be a poorly conditioned problem. This is
brought by propogated data error.

Computational error happening as the algorithm/program is run is something we have far more control over
generally. An algorithm is stable if if the result it produces is relativly insensitive to to changes 
due to approximations made during the computation. (By definition a stable algorithm produces *exactly* 
the correct result for a nearly correct problem)

Accuracy is based on both conditioning and stability. **An accurate solution is only obtained with a problem
that is well conditioned and stable.**

