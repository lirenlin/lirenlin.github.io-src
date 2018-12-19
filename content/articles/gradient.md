Title: Gradient梯度
Date: 2018-12-19
Category: Math
Tags: Math, SLAM

The gradient is a vector-valued function, as opposed to a derivative, which is scalar-valued. 

In some applications it is customary to represent the gradient as a row vector or column vector of its components
in a rectangular coordinate system.


- muti-variable function
	* scalar-valued function $f: \mathbb{R}^n \to \mathbb{R}$, gradient vector, row matrix or column matrix.<br/>
	$f(\mathbf{x})$ where $\mathbf(x) = (x1, x2,...,xn)$.
\begin{align*}
\def\pdiff#1#2{\frac{\partial #1}{\partial #2}}
Df(\mathbf{a}) = \left[\pdiff{f}{x_1}(\mathbf{a}) \ \pdiff{f}{x_2}(\mathbf{a}) \ \ldots \ 
\pdiff{f}{x_n}(\mathbf{a})\right].
\end{align*}
	* vector-valued function $\boldsymbol{f}: \mathbb{R}^n \to \mathbb{R}^m$, mxn matrix. Jacobian matrix.<br\>
\begin{gather*}
\mathbf{f}(\mathbf{x}) = (f_1(\mathbf{x}),f_2(\mathbf{x}), \cdots, f_m(\mathbf{x}))
	=
	\left[\begin{array}{c}
f_1(\mathbf{x})\\f_2(\mathbf{x})\\ \vdots\\ f_m(\mathbf{x})
	\end{array}\right].
\end{gather*}
\begin{gather*}
\def\pdiff#1#2{\frac{\partial #1}{\partial #2}}
D\mathbf{f}(\mathbf{a})=
\left[
	\begin{array}{cccc}
	\displaystyle\pdiff{f_1}{x_1}(\mathbf{a})&
	\displaystyle\pdiff{f_1}{x_2}(\mathbf{a})&
	\ldots &
	\displaystyle\pdiff{f_1}{x_n}(\mathbf{a})\\
		\displaystyle\pdiff{f_2}{x_1}(\mathbf{a})&
		\displaystyle\pdiff{f_2}{x_2}(\mathbf{a})&
		\ldots &
		\displaystyle\pdiff{f_2}{x_n}(\mathbf{a})\\
			\vdots & \vdots & \ddots & \vdots\\
			\displaystyle\pdiff{f_m}{x_1}(\mathbf{a})&
			\displaystyle\pdiff{f_m}{x_2}(\mathbf{a})&
	\ldots &
\displaystyle\pdiff{f_m}{x_n}(\mathbf{a})
	\end{array}
	\right].
\end{gather*}
- Linear approximation to a function
The gradient of a function f from the Euclidean space $\mathbb{R}^n \to \mathbb{R}$
at any particular point x0 in $\mathbb{R}^n$ characterizes the best linear
approximation to f at x0. The approximation is as follows:
    $$f(x) \approx f (x0) + \nabla f(x0) \cdot (x−x0)$$
for x close to x0, where $\nabla f(x0)$ is the gradient of f computed at x0,
and the dot denotes the dot product on Rn.<br/>
This equation is equivalent to the first two terms in the
**multivariable Taylor series expansion** of f at x0.<br/>
The approximation is valid only when the function is differentiable, and can be
used with the points which is very close to x0.<br/>
This could be extended to **multivariable linear approximation** case.<br/>
It describes the **tangent line/plane** over that point.

[mathinsight: linear approximation multivariable](https://mathinsight.org/linear_approximation_multivariable) <br/>
[mathinsight: derivative matrix](https://mathinsight.org/derivative_matrix) <br/>
[Wiki: Gradient](https://en.wikipedia.org/wiki/Gradient) <br/>

