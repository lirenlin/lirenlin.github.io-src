Title: 线性变换的理解
Date: Thu 10 Jan 23:13:22 CET 2019
Category: Math
Tags: Math

给定一个向量x
[数值] = [坐标] x [坐标系统基]

linear transformation可以理解成坐标系统的改变.
例如将x变换到以[v1, v2, ... vn]为basis的系统下，

\begin{aligned}
X &= c_{1}v_{1} + c_{2}v_{2} + ... c_{n}v_{n} \\
X &= [v_{1} v_{2} ... v_{n}] [c_{1} c_{2} ...]^{T} \\
X &= WC  (1)\\
C &= W^{-1}X (2)
\end{aligned}

(2) 为变换，C为X变换后，在新的坐标系下的坐标. $W^{-1]$为变换矩阵。
(1) 为逆变换，在给定C后，恢复在原始坐标系下的数据

所以对于一个好的变换矩阵，需要有下面两个特征

* 快速的矩阵乘法与求逆，这样才可以快速进行运算。例如使用傅里叶变化矩阵的快速傅里叶变换与Wavelet变换矩阵
* 好的压缩特性，尽量少的坐标轴包含尽量多的信息。这样可以忽略不重要的信息，进行降维，实现压缩


[Lec 31 | MIT 18.06 Linear Algebra, Spring 2005](https://www.youtube.com/watch?v=vGkn-3NFGck&t=1709s)


