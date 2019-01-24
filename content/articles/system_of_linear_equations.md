Title: 线性方程组
Date: Wed 26 Dec 10:25:50 CET 2018
Category: Math
Tags: Math

* In general, a system with fewer equations than unknowns has infinitely many
solutions, but it may have no solution. Such a system is known as an
underdetermined system.

* In general(not always), a system with more equations than unknowns has no solution. Such a
system is also known as an overdetermined system.

* In general, a system with the same number of equations and unknowns has a
single unique solution.

\begin{align}
Ax &= b, \\
A^{-1}Ax &= A^{-1}b, \\
x &= A^{-1}b,
\end{align}
如果这个方程有唯一解，变换可逆，A可逆. 这意味着，从b，可以还原应用了变换之前的x。
这个变换是可逆的。


通常有两个形式：

* 方程组个数大于变量数，无确定解，但是找到一个近似系统描述, 常见为拟合
* 方程组有无数解，在满足一定条件的约束下，给定一个目标函数，使其最大或者最小, 优化

线性 or 非线性系统？
