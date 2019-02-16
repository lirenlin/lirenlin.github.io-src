Title: Local parameterization
Date: Sun 13 Jan 22:04:03 CET 2019
Category: Ceres
Tags: Ceres

Parameterization
使用一个表达方式去表达同一个系统的状态/参数.

## Ceres Local Parameterization
In many cases, some parameters lie on a manifold other than Euclidean space, e.g.,
rotation matrices. In such cases, the user can specify the geometry of the local 
tangent space by specifying a LocalParameterization object.

https://groups.google.com/forum/#!topic/ceres-solver/7HfF6DnCv7o


## 参数化
在迭代优化方法中，例如高斯牛顿，每一次迭代有如下 变量更新:
$$ X = X + \Delta X$$
如果X的参数空间没有定义加法，例如旋转矩阵R, 变换矩阵T，或者简单的旋转向量。这就涉及到两个问题，

1. 如何定义局部参数来表示$\Delta X$，也就是所谓的local parameterization。
2. 定义$\boxplus$运算符，用来更新变量。 $ X = X \boxplus \Delta X$。

### 状态变量$X$参数化
X的参数化与$\Delta X$的参数化会不一样。它们有各自的要求。
对于待估计状态参数X，因为需要直接用于计算误差，所以X的表示方式，如果可以有利于计算的表达，
可以减少计算的复杂度。例如位姿的变化，可以表示直接成旋转矩阵乘法。如果是其他的compact的旋转表示方法，
需要每次进行变化，然后应用在坐标上。通常对于最小二乘法，有很多项误差需要计算，
转换本身就这会是一个非常大的运算花销。

同时X的参数会取决于误差函数的定义, 不同的误差函数，会使用参数的不同形式进行计算。
总之，X的参数化，要尽量的减少它在计算误差时的计算量。

### 更新变量$\Delta X$参数化
另一方面，$\Delta X$的参数化，有不同的要求。$\Delta X$的参数话，要求

1. 其所在的解空间平滑可导数。  
**这个性质对于优化方法的收敛速度非常重要。平滑可导，无奇异，使的在寻找增量的时候可以按照最优
的方向寻找。**
2. 最小化代表信息。
	1. 因为$\Delta X$是优化方法求导的目标，其维度越小，Jacobian matrix的
	列越少，相应计算越少。
	2. 有时候利用冗余的信息代表参数，可以简化计算，但是内部参数之间有一定的
	约束关系。如果这个约束关系在优化求解过程当中没有表示出来，很可能产生不合理的解。
	例如三维旋转矩阵有9个维度。

### 计算数值稳定性
在计算过程当中，有很多信息累加的过程，每个累加，都会有数值计算的误差，这些误差会不断积累。
最后会造成数值的不稳定。

例如用四元数表示旋转。如果用角度来参数化，那么每次需要求解正弦余弦值，然后不断累计乘法。得到最后旋转的叠加。
相反，在四元数参数化中，旋转角度的累积是加法，最后只需要做一次转换，然后求得的最终旋转后的结果。整个过程数值
计算更稳定，也能减少很多的计算量。

## $\boxplus$ 用途

在上面提到的，$\boxplus$运算符，供优化框架使用，来实现迭代过程中状态变量的更新。
它用来连接$X$与$\Delta X$两个不同的参数化空间。

这个运算符还有另一个功能，自动求导框架需要使用此运算符来对参数求导。当然你可以提供手动解析求导方式。
