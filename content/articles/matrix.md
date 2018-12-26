Title: 矩阵性质 (From Wiki)
Date: 2018-12-25
Category: Math
Tags: Math

# Square matrix:
In mathematics, a square matrix is a matrix with the same number of rows and columns. An n-by-n matrix is known as a square matrix of order n. Any two square matrices of the same order can be added and multiplied.

Square matrices are often used to represent simple linear transformations, such as shearing or rotation. For example, if R is a square matrix representing a rotation (rotation matrix) and v is a column vector describing the position of a point in space, the product Rv yields another column vector describing the position of that point after that rotation. If v is a row vector, the same transformation can be obtained using vRT, where RT is the transpose of R.

# Identity matrix:
In linear algebra, the identity matrix, or sometimes ambiguously called a unit matrix, of size n is the n × n square matrix with ones on the main diagonal and zeros elsewhere.  It is denoted by $I_n$, or simply by I if the size is immaterial or can be trivially determined by the context.

# Symmetric matrix:
In linear algebra, a symmetric matrix is a square matrix that is equal to its transpose. Formally,$$A = A^T$$

# Diagonal matrx:
In linear algebra, a diagonal matrix is a matrix in which the entries outside the main diagnoal are all zero. The term usually refers to square matrices.

# Triangular matrix
In the mathematical discipline of linear algebra, a triangular matrix is a special kind of square matrix. A square matrix is called **lower triangular** if all the entries above the main diagonal are zero. Similarly, a square matrix is called **upper triangular** if all the entries below the main diagonal are zero. A triangular matrix is one that is either lower triangular or upper triangular. A matrix that is both upper and lower triangular is called a diagonal matrix.

Because matrix equations with triangular matrices are easier to solve, they are very important in numerical analysis. By the LU decomposition algorithm, an invertible matrix may be written as the product of a lower triangular matrix L and an upper triangular matrix U if and only if all its leading principal minors are non-zero.

# Invertible matrix
In linear algebra, an n-by-n square matrix A is called invertible (also nonsingular or nondegenerate) if there exists an n-by-n square matrix B such that
$$\mathbf {AB} =\mathbf {BA} =\mathbf {I}$$
where In denotes the n-by-n identity matrix and the multiplication used is ordinary matrix multiplication. If this is the case, then the matrix B is uniquely determined by A and is called the inverse of A, denoted by $A^{−1}$.

A square matrix that is not invertible is called singular or degenerate. A square matrix is singular if and only if its determinant is 0. Singular matrices are rare in the sense that a square matrix randomly selected from a continuous uniform distribution on its entries will almost never be singular.

The set of $n × n$ invertible matrices together with the operation of matrix multiplication form a group, the general linear group of degree n.

# Positive-definite matrix
In linear algebra, a symmetric $n × n$ real matrix $M$ is said to be positive definite if the scalar $z^{\textsf {T}}Mz$ is strictly positive for every non-zero column vector $z$ of $n$ real numbers. Here $z^{\textsf {T}}$ denotes the transpose of $z$.

# Orthogonal matrix
An orthogonal matrix is a square matrix whose columns and rows are orthogonal unit vectors (i.e., orthonormal vectors), i.e.
    $$Q^TQ=QQ^T = I$$
where $I$ I is the identity matrix.  
This leads to the equivalent characterization: a matrix Q is orthogonal if its transpose is equal to its inverse:
$$Q^{\mathrm {T} }=Q^{-1}$$  
An orthogonal matrix Q is necessarily invertible (with inverse $Q^−1 = Q^T$), unitary ($Q^−1 = Q^∗$) and therefore normal ($Q^∗Q = QQ^∗$) in the reals. The determinant of any orthogonal matrix is either +1 or −1. As a linear transformation, an orthogonal matrix preserves the dot product of vectors, and therefore acts as an isometry of Euclidean space, such as a rotation, reflection or rotoreflection. In other words, it is a unitary transformation.  
The set of n × n orthogonal matrices forms a group O(n), known as the orthogonal group. The subgroup SO(n) consisting of orthogonal matrices with determinant +1 is called the special orthogonal group, and each of its elements is a special orthogonal matrix. As a linear transformation, every special orthogonal matrix acts as a rotation. 

# Unitary matrix (酉矩阵)
In mathematics, a complex square matrix U is unitary if its conjugate transpose $U^*$ is also its inverse—that is, if
$$U^∗ U = U U^∗ = I$$
where $I$ is the identity matrix. 
