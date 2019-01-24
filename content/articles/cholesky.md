Title: cholesky decomposition
Date: Tue 22 Jan 16:48:47 CET 2019
Category: Math
Tags: Math


* Linear least squares, the solution is to solve this system of linear
equations: $A^TAx = TX = A^Tb$

* Non-linear least squares problem via iterative method
	* Gauss-Newton Method, solve $(J_x^T J_x)\Delta = T\Delta = -J_x^Tf(x)$
	* Levenberg-Marquardt Algorithm, solve $(J_x^T J_x + \lambda D)\Delta = T\delta = -J_x^Tf(x)$

在上面所有的T都是symmetric矩阵，可以使用Cholesky decomposition来解决。

* 减少计算量, 即使有额外的中间步骤需要计算
* the amount of fill-in which occours when computing a matrix decomposition of a sparse matrix
* stable

Cholesky decomposition $A = LL^T$. This is stable even without
pivoting, and hence extremely simple to implement.
It is the standard decomposition method for almost all unconstrained optimization
problems including bundle adjustment, as the Hessian is positive definite near
a non-degenerate cost minimum (and in the Gauss-Newton approximation, almost
everywhere else, too). If A is symmetric but only positive semidefinite,
diagonally pivoted Cholesky decomposition can be used.

Another notable method is that based on QR decomposition, which is up to a
factor of two slower than the normal equations, but much less sensitive to
ill-conditioning in J.

The triangular factor L and a solution to a corresponding linear system may not
be accurate enough because of machine arithmetic. In order to refine the
solution, a number of iterative methods (for example, the conjugate
 gradient method) can be employed using the $LL^T$ decomposition as a
preconditioner.  The memory saving is the main reason to use an incomplete or
inaccurate decomposition as a preconditioner.[^1]


[^1]:https://algowiki-project.org/en/Cholesky_method
