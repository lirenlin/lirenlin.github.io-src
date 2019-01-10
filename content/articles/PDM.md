Title: Positive definite matrix
Date: Wed  9 Jan 16:03:03 CET 2019
Category: Math
Tags: Math, Optimization

# Definition[^1]
In linear algebra, a **symmetric** $n \times n$ real matrix $M$ is said to be
positive definite if the scalar $z^{T}Mz$ is strictly positive for every
non-zero column vector $z$ of $n$ real numbers. Here $z^{\textsf {T}}$ denotes
the transpose of $z$.

More generally, an $n \times n$ Hermitian matrix $M$ is said to be positive
definite if the scalar $z^{*}Mz$ is strictly positive for every non-zero column
vector $z$ of $n$ complex numbers. Here $z^{*}$ denotes the conjugate transpose
of $z$. Note that $z^{∗} M z$ is automatically real since $M$ is Hermitian.

# 与Diagonalization, eigenvalues和eigenvectorg关系

# Quadratic forms, convexity, optimization[^1]
The (purely) quadratic form associated with a real $n\times n$ matrix M is the
function $Q : \mathbb {R}^n \to \mathbb R$ such that $Q(x)=x^{T}Mx$ for all
$x$. $M$ can be assumed symmetric by replacing it with  $1/2(M+M^{T})$.

A symmetric matrix $M$ is positive definite if and only if its quadratic form
is a strictly **convex** function.

More generally, any quadratic function from $\mathbb {R}^{n}$ to $\mathbb {R}$
can be written as $ x^{T}Mx+x^{T}b+c$ where $M$ is a symmetric $n\times n$
matrix, $b$ is a real $n$-vector, and $c$ a real constant. This quadratic
function is strictly convex, and hence has a unique finite global minimum, if
and only if $M$ is positive definite. For this reason, positive definite
matrices play an important role in optimization problems.


#Additional information:
[StackExchange: Why are symmetric positive definite (SPD) matrices so important?](https://stats.stackexchange.com/questions/224005/why-are-symmetric-positive-definite-spd-matrices-so-important)

[Eigenvectors and Eigenvalues: Explained Visually](http://setosa.io/ev/eigenvectors-and-eigenvalues/)

[^1]: https://en.wikipedia.org/wiki/Definiteness_of_a_matrix
