Title: Variance, gradient, Jacobian and Hessian matrix 记忆
Date: 2018-12-18
Category: math
Tags: math, SLAM

Jacobian矩阵　用于一阶梯度下降法<br/>
Hessian矩阵，用于二阶牛顿法<br/>
高斯牛顿法，使用J<sup>T</sup>J作为牛顿法中二阶Hessian矩阵的近似，　从而省略了计算Ｈ的过程<br/>
[下面这个文章介绍了Jacobian与Hessian矩阵的关系用途](http://jacoxu.com/jacobian%E7%9F%A9%E9%98%B5%E5%92%8Chessian%E7%9F%A9%E9%98%B5/)


Hessian是对称矩阵<br/>
[jacobian, Hassian and gradient关系](https://blog.csdn.net/dsbatigol/article/details/12558891)

covariance,协方差：<br/>
$$cov(X,Y) = E((X-\mu)(Y-\nu)) = E(X \cdot Y) - \mu\nu$$

variance, 方差：　二阶矩<br/>
 一个随机变量的方差描述的是它的离散程度，也就是该变量离其期望值的距离, $\mu=E[X]$
$$Var(X) = cov(X, X)$$
$$Var(X) = E[(X-\mu)^2]$$

期望：　一阶矩<br/>
[方差Wiki](https://zh.wikipedia.org/wiki/%E5%8D%8F%E6%96%B9%E5%B7%AE)

