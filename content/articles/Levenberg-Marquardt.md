Title: Leventberg-Marquardt Algorithm
Date: Fri 25 Jan 12:31:55 CET 2019
Category: Math
Tags: Math

最近想弄懂LM算法，看了一些介绍。 虽然不重要，但是对于它到底是使用line search和trust region算法感到困惑。

> Levenberg (1944) and later Marquardt (1963) suggested to use a
damped Gauss-Newton method, cf Section 2.4.  The step $h_{lm}$ is defined by the
following modification to (3.9),[^1]
$$(J^TJ + \lambda I)h_{lm} = -g \;with\; g = J^Tf \;and\; \lambda \geqslant 0$$

所以，最初LM算法的提出是以一种damped Gauss-Newton的方式， 而没有使用trust
region的概念。

> The above algorithm has the disadv antage that if the value of $lambda$ is large,
the calculated Hessian matrix is not used at all.  We can deri ve some advantage
out of the second deri vative even in such cases by scaling each component of
the gradient according to the curv ature.  This should result in lar ger movement
along the directions where the gradient is smaller so that the classic
“error valley” problem does not occur any more.  This crucial insight was
provided by Marquardt.  He replaced the identity matrix in (7) with the diagonal
of the Hessian resulting in the Levenberg-Marquardt update rule.  [^2]
$$(H + \lambda diag[H])h_{lm} = -g \;with\; g = J^Tf \;and\; \lambda \geqslant 0$$

同时它是一个基于经验(heuristic)的算法, 是从gradient
descent和Gauss-Newton算法总观察改进而来。

* gradient descent一阶算法简单, 快速，但是有各种收敛问题,
  确定的方向，但是更新步长没有根据梯度变化而调整。
* 同时牛顿法为二阶，使用second derivative。从几何上说，牛顿法就是用一个二次曲面
去拟合你当前所处位置的局部曲面，而梯度下降法是用一个平面去拟合当前的局部曲面，
通常情况下，二次曲面的拟合会比平面更好，所以牛顿法选择的下降路径会更符合真实的
最优下降路径。由于精确的Hessian矩阵求解计算量大，可以使用: $H \approx J^TJ$
近似Hessian矩阵，这就是Gauss-Newton算法。但是高斯牛顿算法有一个问题在于，对于初始点比较敏感。

结合二者的优缺点，提出的LM算法，根据$\lambda$的值相对大小，
LM算法体现出梯度下降或者高斯牛顿算法的特征，同时根据误差计算，调整damping factor
$\lambda$大小。

**但是，这个经验公式在实际问题中，却非常有效。因为它跟基于trust region的高斯牛顿
法得到的迭代公式完全一样。所以有了优化的理论根据！**

# LM算法基本流程


# 基于信赖域的Gauss-Newton法推导
## non-linear least squares problem
总是把对不同函数的求导弄混，这里重写写一遍，加深理解。
$$\newcommand{\xv}{\mathbf{x}}
\xv^{*} = argmin_{\xv}\{F(\xv)\}$$
where
$$\newcommand{\xv}{\mathbf{x}} \newcommand{\fv}{\mathbf{f}}
F(\xv)=\frac{1}{2}\sum_{i=1}^{m}(f_{i}(x))^2\;=\;
\frac{1}{2}\Vert \fv(\xv) \Vert^2\;=\;
\frac{1}{2}\fv(\xv)^{T}\fv(\xv)$$

根据泰勒展开：
$$\newcommand{\xv}{\mathbf{x}} \newcommand{\hv}{\mathbf{h}}
\newcommand{\fv}{\mathbf{f}}
\fv(\xv+\hv) \;=\; \fv(\xv) + \mathbf{J}(\xv)\hv + O(\Vert \hv \Vert )^2 $$
这里$\mathbf{J}$为$\mathbf{f}(\mathbf{x})$的Jacobian矩阵(不是$F(\mathbf{x})$)。
$$\newcommand{\xv}{\mathbf{x}} \newcommand{\fv}{\mathbf{f}}
\def\pdiff#1#2{\frac{\partial #1}{\partial #2}}
\pdiff{F}{x_j}(\xv) \;=\; \sum_{i=1}^{m}f_{i}(\xv)\pdiff{f_i}{x_j}(\xv) \\
F^{'}(\xv) \;=\; J(\xv)^{T}\fv(\xv)$$

对$\mathbf{f}$泰勒展开
$$\newcommand{\xv}{\mathbf{x}} \newcommand{\hv}{\mathbf{h}}
\newcommand{\fv}{\mathbf{f}} \newcommand{\jv}{\mathbf{J}}
\fv(\xv + \hv) \;=\; \ell(\hv) \approx \fv(\xv) + \mathbf{J}(\xv)\hv \\
F(\xv+\hv) \;=\; L(\hv) \;=\; \frac{1}{2}\ell(\hv)^{T}\ell(\hv) \\
=\; \frac{1}{2}{\fv}^T\fv + {\hv}^T\jv\fv + \frac{1}{2}{\hv}^T{\jv}^T\hv \\
=\; F(\xv) + {\hv}^T{\jv}^T\fv + \frac{1}{2}\hv^T{\jv}^T\jv\hv
=\; F(\xv) + {\fv}^T{\jv}\hv + \frac{1}{2}\hv^T{\jv}^T\jv\hv
$$
$L$的gradient与Hessian为:
$$\newcommand{\xv}{\mathbf{x}} \newcommand{\hv}{\mathbf{h}}
\newcommand{\fv}{\mathbf{f}} \newcommand{\jv}{\mathbf{J}}
L^{'} \;=\; \jv^T\fv + \jv^T\jv\hv, ;\ L^{''} \;=\; \jv^T\jv$$
对于高斯牛顿法，求$\mathbf{h}_{gn}$使得$L(\mathbf{h})$最小：
$$\newcommand{\hv}{\mathbf{h}}
\newcommand{\jv}{\mathbf{J}}
\newcommand{\fv}{\mathbf{f}}
\hv_{gn} \;=\; argmin_{\hv}{L(\hv)} \\
L^{'}(\hv) \;=\; 0 \\
({\jv}^T\jv)\hv_{gn} \;=\; -{\jv}^T\fv
$$

## 基于信赖域的Gauss-Newton法推导
$$L({\Delta x_k}) = F(x_k + \Delta x_k) \approx f(x_k) + J_{x_k}{\Delta x_k} + \frac{1}{2}{\Delta x_k}H_{x_k}{\Delta x_k}$$
求解子问题：
$$argmin_{\Delta x_k} L({\Delta x_k}), \; s.t. \Vert D\Delta x_k \Vert^2 \leq \mu \; (1)$$
信赖域法的核心问题是一个不等式约束问题，可以通过Lagrange将它转换成一个无约束问题。
$$argmin_{\Delta x_k} L({\Delta x_k}) \;+\; \frac{\lambda}{2}\Vert D\Delta x_k \Vert^2\; (2)$$
$\lambda$为Lagrange乘子。展开得：
$$(H + \lambda D^TD)\Delta x_k \;=\; -g \;with\; g = J^Tf$$
当去D为单位矩阵I时，得到的更新求解公式与之前的经验公式一样。
[The trust region subproblem](http://pages.mtu.edu/~msgocken/ma5630spring2003/lectures/tr/tr/node2.html)


#注意点

* $lambda$取值要使得$(\mathbf{J}^T\mathbf{J} + \lambda I)$为正定矩阵positive
definit, 这样$\Delta x_k$才是$L$的minimizer.
* 关于D的选取，有的选取为单位矩阵，有的选取为Hessian矩阵对角元素
* $(H + \lambda diag H) 的condition number可能会很大[^3]。或者因为精度问题，导致H对
角线上元素为0. 对这个表达式进行矩阵分解求解方程的时候，需要注意算法的stability.
(可能考虑使用QR decomposition[^3])


这里有个一LM的算法实现，注意上面提到的两点
https://gist.github.com/lirenlin/ce6159058348efa1a9f7c8d621c1e768

[^1]: [methods for non-linear least squares problems](orbit.dtu.dk/files/2721358/imm3215.pdf)
[^2]: [The Levenberg-Marquardt Algorithm ](http://ananth.in/docs/lmtut.pdf)
[^3]: https://sites.math.washington.edu/~reu/papers/2009/mark/REU%20Final%20Paper.pdf
[^4]: https://mathoverflow.net/questions/106277/levenberg-marquadt-near-the-minima-for-non-zero-residual-problems://mathoverflow.net/questions/106277/levenberg-marquadt-near-the-minima-for-non-zero-residual-problems/ 
