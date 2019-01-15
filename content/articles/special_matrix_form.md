Title: "美"的矩阵
Date: Wed  9 Jan 16:56:43 CET 2019
Category: Math
Tags: Math

"美"的矩阵形式
# identity matrix 单位矩阵
# Unitary matrix 酉矩阵
# Normal matrix 正规矩阵

# Orthogonal matrix[^1]
An orthogonal matrix is a square matrix whose columns and rows are orthogonal
unit vectors (i.e., orthonormal vectors), i.e.
$$Q^{T} Q = Q Q^{T} = I$$
where $I$ is the identity matrix.
This leads to the equivalent characterization: a matrix Q is orthogonal if
its transpose is equal to its inverse:
$$Q^{T} = Q^{−1}. $$

An orthogonal matrix Q is necessarily invertible (with inverse $Q^{−1} = Q^{T}$),
unitary ($Q^{−1} = Q^{∗}$) and therefore normal ($Q^{∗}Q = QQ^{∗}$) in the reals.
The determinant of any orthogonal matrix is either +1 or −1. As a linear
transformation, an orthogonal matrix preserves the dot product of vectors, and
therefore acts as an isometry of Euclidean space, such as a rotation, reflection
or rotoreflection. In other words, it is a unitary transformation.

The set of n × n orthogonal matrices forms a group $O(n)$, known as
the orthogonal group. The subgroup $SO(n)$ consisting of orthogonal
matrices with determinant +1 is called the special orthogonal
group, and each of its elements is a special orthogonal matrix. As
a linear transformation, every special orthogonal matrix acts as a
rotation.

## Decompositions
A number of important matrix decompositions (Golub & Van Loan 1996) involve
orthogonal matrices, including especially:

* QR decomposition  
    M = QR, Q orthogonal, R upper triangular
* Singular value decomposition  
    M = UΣVT, U and V orthogonal, Σ diagonal matrix
* Eigendecomposition of a symmetric matrix (decomposition according to the spectral theorem)  
    S = QΛQT, S symmetric, Q orthogonal, Λ diagonal
* Polar decomposition  
    M = QS, Q orthogonal, S symmetric non-negative definite

# diagonal matrix
## diagonal matrix with eigenvalue

# orthonormal matrix

# symmetric matrix:
A symmetric matrix is a square matrix that is equal to its transpose. Formally,
$$A^{T} = A$$
A nxn symmetric matrix A not only has a nice structure, but it also satisfies
the following (can be diagonaized, S = QΛQT, S symmetric, Q orthogonal, Λ diagonal):

* A has exactly n (not necessarily distinct) eigenvalues
* There exists a set of n eigenvectors, one for each eigenvalue, that are mututally orthogonal.

Thus, the situation encountered with the matrix D in the example above cannot
happen with a symmetric matrix: A symmetric matrix has n eigenvalues and there
exist n linearly independent eigenvectors (because of orthogonality) even if
the eigenvalues are not distinct.

Proof of eigenvalue properties of the real symmetric matrix[^2].


> 矩阵的相似变换可以把一个比较丑的矩阵变成一个比较美的矩阵，而保证这两个矩阵都是描述了同一个线性变换。至于什么样的矩阵是“美”的，什么样的是“丑”的，我们说对角阵是美的。在线性代数中，我们会看到，如果把复杂的矩阵变换成对角矩阵，作用完了之后再变换回来，这种转换很有用处，比如求解矩阵的n次幂！而学了矩阵论之后你会发现，矩阵的n次幂是工程中非常常见的运算。这里顺便说一句，将矩阵对角化在控制工程和机械振动领域具有将复杂方程解耦的妙用！总而言之，相似变换是为了简化计算！

> 从另一个角度理解矩阵就是：矩阵主对角线上的元素表示自身和自身的关系，其他位置的元素aij表示i位置和j位置元素之间的相互关系。那么好，特征值问题其实就是选取了一组很好的基，就把矩阵 i位置和j位置元素之间的相互关系消除了。而且因为是相似变换，并没有改变矩阵本身的特性。因此矩阵对角化才如此的重要！

# similar matrix:
* have same eigenvalues
* matrices represent the same thing in different basis

# projection matrix:
In linear algebra and functional analysis, a projection is a linear
transformation P from a vector space to itself such that $P^2 = P$. That is,
whenever P is applied twice to any value, it gives the same
result as if it were applied once (idempotent). It leaves its
image unchanged.[1] Though abstract, this definition of
"projection" formalizes and generalizes the idea of graphical
projection. One can also consider the effect of a projection on
a geometrical object by examining the effect of the projection
on points in the object.

[^1]:https://en.wikipedia.org/wiki/Orthogonal_matrix 
[^2]: http://farside.ph.utexas.edu/teaching/336k/Newton/node66.html
