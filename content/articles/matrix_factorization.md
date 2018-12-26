Title: 矩阵分解
Date: 2018-12-25
Category: Math
Tags: Math


# Simplify the computation of linear system of equations.
Matrix factorization in the context of numerical linear algebra(NLA) generally serves the purpose of rephrasing through a series of easier subproblems a task that may be relatively difficult to solve in its original form.

 For example, given the typical linear system Ax = b for $A \in \mathbb {R}^{n × n}$, x and b $\in \mathbb {R}^n$ , a factorization of A as LU for L a unit lower triangular matrix (thus, with ones along its main diagonal) and an upper triangular U is a mechanism for characterizing what occurs in Gaussian elimination.

 We replace $Ax = b$ by two (easier to solve) triangular systems:  find y so $Ly = b$ and then find x so $Ux = y$.The point being made here is that the factorization of A as LU has no real importance in and of itself other than as a computationally convenient means for obtaining a solution to the original linear system.

# Help to understand the structure of a big data matrix.
Typically, a matrix $A \in \mathbb {R}^{n × p}$ represents a data matrix containing numerical observations on n objects (subjects) over p attributes (variables), or possibly $B \in \mathbb {R}^{p × p}$ and the entries are some measure of proximity between attributes, such as the correlation between columns of A.

The major purpose of a matrix factorization in this context is to obtain some form of lower-rank (and therefore simplified) approximation to A (or possibly to B) for understanding the structure of the data matrix, particularly the relationship within the objects and within the attributes, and how the objects relate to the attributes. If we can further interpret the matrix factorization geometrically and actually present the results spatially through coordinates obtained from the components of the factorization, we will be able to better communicate to others what structure may be present in the original data matrix.

In any case, matrix factorizations are again directed toward the issue of simplicity, but now the actual components making up a factorization are of prime concern and not solely as a mechanism for solving another problem.


# Related concepts
* [Rank (linear algebra)秩](https://en.wikipedia.org/wiki/Rank_(linear_algebra))
> In linear algebra, the rank of a matrix A is the dimension of the vector space generated (or spanned) by its columns.[1] This corresponds to the maximal number of linearly independent columns of A.
* [Numerical stability](https://en.wikipedia.org/wiki/Numerical_stability)

# Related articles
[Two Purposes for Matrix Factorization: A Historical Appraisal](http://staff.ustc.edu.cn/~ynyang/group-meeting/2014/matrix-factorization/hubert.pdf)  
[Linear Algebra and Matrix Decompositions](https://people.duke.edu/~ccc14/sta-663/LinearAlgebraMatrixDecompWithSolutions.html)

[奇异值分解简介：从原理到基础机器学习应用](https://www.jiqizhixin.com/articles/0301)
