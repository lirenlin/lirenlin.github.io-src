Title: Quadratic forms
Date: Sun 27 Jan 13:47:50 CET 2019
Category: Math
Tags: Math

最近在凸优化[^1]一书中，steepest descent相关章节看到quadratic norm(9.4)，
gradient descent与steepest descent的却别就在于不同范数(norm)的选取
>
$$\Delta_{nsd}=argmin_v(\nabla f(x)^Tv\mid \|v\|<=1)$$
> i.e.  , as the direction in the unit ball of ‖·‖ that extends farthest in the
> direction $-\nabla f(x)$  
> Steepest descent for quadratic norm  
> We consider the quadratic norm
> $$\Vert z \Vert_{P} = (z^T P z)^{1/2} = \Vert P^{1/2}z\Vert_{2}$$

不太清楚它的形式，找到如下资料[^2]

<img src="images/quadratic_forms_1.png" alt="quadratic forms" title="" style="max-width:80%; max-height:80%"/>
<img src="images/quadratic_forms_2.png" alt="quadratic forms" title="" style="max-width:80%; max-height:80%"/>
<img src="images/quadratic_forms_3.png" alt="quadratic forms" title="" style="max-width:80%; max-height:80%"/>


[^1]: http://stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf
[^2]: https://see.stanford.edu/materials/lsoeldsee263/15-symm.pdf
[^3]: [梯度下降法和最速下降法的细微差别](https://blog.csdn.net/Timingspace/article/details/5096356://blog.csdn.net/Timingspace/article/details/50963564 )
