Title: 简单BA代码分析
Date: Tue 15 Jan 08:36:12 CET 2019
Category: SLAM
Tags: BundleAdjustment

简单代码分析，帮助自己从概念到代码的理解。代码使用Eigen, ceres solver第三方软件库。

# 问题假设

输入：

* $P^{c}_{ij}$: 路标(point)j在i相机位姿下，在相机坐标下的观测坐标$[Px^{c} Py^{c}]^T$(观测数据)
* $T_{i} = [rotation matrix, translation]\in \mathbb {R}^{6}$ 或者$T = [Quaternion, translation] \in \mathbb {R}^{7}$ 相机位姿(pose)初始估计 (前端计算数据)
* $P^{w}_{j} = [Px^{w} Py^{w} Pz^{w}]$路标(point)在世界坐标系下的初始估计值(前端计算数据)

输出：

* 经过调整后相机的位姿(pose)
* 与调整后的路标在世界坐标系下的坐标。

$$ \overline {P^{c}_{ij}} = h(T_{i}, P^{w}_{ij})$$
给定相机位姿，路标世界坐标，计算投影坐标$h : SE(3) × \mathbb {R}^{3} \to \mathbb {R}^{2}$
因为投影为平面，所以只有二维，世界坐标维三维。

cost function, reprojection error:
$$ e = \sum_{i} {\sum_{j} {\Vert(h(T_{i}, P^{w}_{ij}) - P^{c}_{ij})\Vert^2}}$$

$h$这里可以分为两步
\begin{align*}
P^{w'} &= f(T, P^{w}) = TP^{w} = RP^{w} + t: \mathbb {R}^3 \to \mathbb {R}^3 \\
\overline {P^{c}} &= g(P^{w'}) = [\frac {Px^{w'}}{Pz^{w'}} \frac{Py^{w'}}{Pz^{w'}}]^T: \mathbb {R}^3 \to \mathbb {R}^2 \\
\overline {P^{c}} &= g(f(T, P^{w}))
\end{align*}

非线性最小二乘优化，迭代方法，需要求得对于优化标量偏导Jacobian矩阵,
  以及迭代更新计算。这里，优化的变量为位姿$T \in \mathbb {R}^6$与$P^{w} \in
  \mathbb {R}^3$

# cost function Jabian矩阵推导
根据求导chain rule:
\begin{align*}
\def\pdiff#1#2{\frac{\partial #1}{\partial #2}}
1)\; \pdiff{h}{P^{w}} &= \pdiff{g(P^{w'})}{f}\pdiff{f}{P^{w}}\\
2)\; \pdiff{h}{T} &= \pdiff{g(P^{w'})}{f}\pdiff{f}{T}\\
\end{align*}

\begin{gather*}
\def\pdiff#1#2{\frac{\partial #1}{\partial #2}}
\pdiff{g(P^{w'})}{f} &= 
\left[
  \begin{array}{ccc}
  \frac {1}{Pz^{w'}} & 0 & \frac {Px^{w'}}{(Pz^{w'})^2} \\
  0 & \frac {1}{Pz^{w'}} & \frac {Py^{w'}}{(Pz^{w'})^2} \\
  \end{array}
\right] = \frac {1}{Pz^{w'}}
\left[
  \begin{array}{ccc}
  1 & 0 & \frac {Px^{w'}}{Pz^{w'}} \\
  0 & 1 & \frac {Py^{w'}}{Pz^{w'}} \\
  \end{array}
\right]
\end{gather*}

这里2)的导数在SE(3)空间无法计算，因为没有定义的加法，因此使用lie group与lie
algebra计算。
\begin{align*}
\def\pdiff#1#2{\frac{\partial #1}{\partial #2}}
\pdiff{f}{T} \to \pdiff{TP}{\delta\xi}
&= \lim_{\delta\xi \to 0}{\frac {exp(\delta\xi^{\wedge})exp(\xi^{\wedge})P -exp(\xi^{\wedge})P}{\delta\xi}} \\
&\approx \lim_{\delta\xi \to 0}{\frac {(I + \delta\xi^{\wedge})exp(\xi^{\wedge})P -exp(\xi^{\wedge})P}{\delta\xi}} \\
&= \lim_{\delta\xi \to 0}{\frac {\delta\xi^{\wedge}exp(\xi^{\wedge})P}{\delta\xi}} \\
&= \lim_{\delta\xi \to 0}{\frac
      {\left [\begin{array}{cc} \delta\varphi^{\wedge} & \delta\rho \\ 0^T & 0 \\ \end{array} \right] \left[ \begin{array}{c} RP + t \\ 1 \end{array} \right]}
      {\delta\xi}} \\
&= \lim_{\delta\xi \to 0}{\frac
      {\left[ \begin{array}{c} \delta\varphi^{\wedge}(RP + t) + \delta\rho \\ 0 \end{array} \right]}
      {\delta\xi}}
\end{align*}

T对应的李代数为$\delta\xi = [\delta\varphi \; \delta\rho]^T$, 对他们按顺序求导得到
\begin{align*}
\def\pdiff#1#2{\frac{\partial #1}{\partial #2}}
\pdiff{f}{T} \to \pdiff{TP}{\delta\xi}
&= \lim_{\delta\xi \to 0}{\frac
      {\left[ \begin{array}{c} \delta\varphi^{\wedge}P^{w'} + \delta\rho \\ 0 \end{array} \right]}
      {\delta\xi}} \\
&= \lim_{\delta\xi \to 0}{\frac
      {\left[ \begin{array}{c} -{P^{w'}}^{\wedge}\delta\varphi + \delta\rho \\ 0 \end{array} \right]}
      {\delta\xi}} \\
&= \left[ \begin{array}{cc} -{P^{w'}}^{\wedge} & I \\ 0^T & 0^T \end{array} \right]
\end{align*}

推导过程与这里想吻合，具体计算可以参考这里代码.

[Visual SLAM Tutorial: Bundle Adjustment]({filename}/pdfs/Visual_SLAM_Tutorial_Bundle_Adjustment.pdf)  
[github source code fork](https://github.com/lirenlin/ba_demo_ceres)

# 优化参量更新
注意这里对李代数求导，对于原参数的更新，必须返回到SE(3)。
$$X = X + \Delta X$$
这里$\Delta X$是用Jacobian矩阵求得。因为位姿相关部分是用李代数求得，所以$\Delta X$位姿更新部分也是李代数，
在更新T参数时，需要变换到SE(3)下。对于路标位置，可以直接更新。
这个使用ceres solver里面的LocalParameterization实现，重载plus成员函数。

从李代数到Transform matrix的转换在《视觉slam十四讲》李代数章节讲的很清楚。

# 代码备注
Eigen库里面有大量的运算符重载，例如四元数表示的旋转可以直接与三维坐标想成得到旋转后的向量。
在数学上是不行的。

# 参考资料

* 《视觉slam十四讲》  
* [Visual SLAM Tutorial: Bundle Adjustment]({filename}/pdfs/Visual_SLAM_Tutorial_Bundle_Adjustment.pdf)  
* [github source code fork](https://github.com/lirenlin/ba_demo_ceres)  

