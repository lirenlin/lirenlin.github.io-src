Title: line search
Date: Wed 19 Dec 22:23:31 GMT 2018
Category: Math
Tags: Math, SLAM

From [Wiki](https://en.wikipedia.org/wiki/Line_search)
> In optimization, the line search strategy is one of two basic iterative 
approaches to find a local minimum $\mathbf {x}^{*}$ of an objective function
$\mathbf {f} :\mathbb {R} ^{n} \to \mathbb {R}$. The other approach is 
[trust region](https://en.wikipedia.org/wiki/Trust_region).

> The line search approach first finds a descent direction along which the 
objective function $f$ will be reduced and then computes a 
step size that determines how far $\mathbf {x}$ should move along that 
direction. The descent direction can be computed by various methods, such as 
gradient descent, Newton's method and Quasi-Newton method. The step size can be 
determined either exactly or inexactly. 

> trust-region methods first choose a step size (the size of the trust region) 
and then a step direction, while line-search methods first choose a step 
direction and then a step size. 

gradient descent, 一阶偏导, jacobian matrix<br/>
Newtone method, 二阶偏导, Hessian matrix<br/>
Guass-Newton method, 使用Jacobian matrix近似Hessian matrix $\mathbf {H} \approx 2\mathbf {J_r^T} \mathbf{J_r}$


[Wiki: gradient descent](https://en.wikipedia.org/wiki/Gradient_descent)<br/>
[【最优化】一文搞懂最速下降法](https://zhuanlan.zhihu.com/p/32709034)
