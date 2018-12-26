Title: 矩阵乘法
Date: 2018-12-25
Category: Math
Tags: Math

$$C = AB, A \in \mathbb {R}^{m \times n}, b \in \mathbb {R}^{n \times l}, c \in \mathbb {R}^{m \times l}$$

For example:
$$
A =
\begin{bmatrix}
a_{00} & a_{01} & a_{02}\\
a_{10} & a_{11} & a_{12}\\
a_{20} & a_{21} & a_{22}
\end{bmatrix}
B =
\begin{bmatrix}
b_{00} & b_{01} & b_{02}\\
b_{10} & b_{11} & b_{12}\\
b_{20} & b_{21} & b_{22}
\end{bmatrix}
C =
\begin{bmatrix}
c_{00} & c_{01} & c_{02}\\
c_{10} & c_{11} & c_{12}\\
c_{20} & c_{21} & c_{22}
\end{bmatrix}
$$


# Componenet wise
$$C_{ij} = \sum_{k=1}^{m} a_{ik} \times b_{kj}$$
for i = 1, ..., m and j = 1, ..., l.

# Row wise
Row of C is the combination of rows of B

$$
\begin{cases}
c_{00} = a_{00} \times b_{00} + a_{01} \times b_{10} + a_{02} \times b_{20} \\
c_{01} = a_{00} \times b_{01} + a_{01} \times b_{11} + a_{02} \times b_{21} \\
c_{03} = a_{00} \times b_{02} + a_{01} \times b_{12} + a_{02} \times b_{22} \\
\end{cases} \rightarrow
\begin{bmatrix}
c_{00} \\ c_{01} \\ c_{02}
\end{bmatrix}^T =
\begin{bmatrix}
b_{00} \\ b_{01} \\ b_{02}
\end{bmatrix} ^T
\times  a_{00} +
\begin{bmatrix}
b_{10} \\ b_{11} \\ b_{12}
\end{bmatrix}^T
\times  a_{01} +
\begin{bmatrix}
b_{20} \\ b_{21} \\ b_{22}
\end{bmatrix}^T
\times  a_{02}
$$

#Column wise
Column of C is the combination of columns of A
$$
\begin{cases}
c_{00} = a_{00} \times b_{00} + a_{01} \times b_{10} + a_{02} \times b_{20} \\
c_{10} = a_{10} \times b_{00} + a_{11} \times b_{10} + a_{12} \times b_{20} \\
c_{20} = a_{20} \times b_{00} + a_{21} \times b_{10} + a_{22} \times b_{20} \\
\end{cases} \rightarrow
\begin{bmatrix}
c_{00} \\ c_{10} \\ c_{20}
\end{bmatrix} =
\begin{bmatrix}
a_{00} \\ a_{10} \\ a_{20}
\end{bmatrix}
\times  b_{00} +
\begin{bmatrix}
a_{01} \\ a_{11} \\ a_{21}
\end{bmatrix}
\times  b_{10} +
\begin{bmatrix}
a_{02} \\ a_{12} \\ a_{22}
\end{bmatrix}
\times  b_{20}
$$

# Matrix wise
AB is the sum of col_of(A) * row_of(B)
$$AB = \sum_{i=0}^l {A[:i] \times B[i:]}$$
where $a[:i] \in \mathbb {R}^{mx1}, B[i:] \in \mathbb {R}^{1xl}$


# Block matrix multiplication
[Wiki](https://en.wikipedia.org/wiki/Block_matrix#Block_matrix_multiplication)
