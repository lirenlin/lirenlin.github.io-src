Title: Graph SLAM总结
Date: Thu 14 Feb 16:21:45 CET 2019
Category: SLAM
Tags: SLAM

## Vertex
图的顶点，代表待优化的变量，具体表示形式取决于参数化(parameterazation)。

顶点可以是多种形式，例如SLAM问题中的机器人位姿(pose)，或者路标的坐标(三维空间$[x,y,z]$，或者二维空间坐标$[x,y]$)。同时，位姿也可以用不同的参数表达，可以是两个位姿间的变化矩阵$T$，或者是3DoF下的位置与转角$[x,y,\theta]$。可以融合多种信息，统一求解，非常的灵活。

## Edge
相应的，不同顶点之间，需要合适的边连接起来，表示它们之间的约束与变换。这个需要与顶点的性质统一。

例如，位姿顶点之间，是通过运动方程的边连接。位姿顶点与路标顶点，是通过观测方程连接。在没有相关信息的时候，也可以通过其他信息推导。例如在没有运动方程信息的时候，可以通过scan to scan match来获取pose之间的估计。但是，总体来说，信息越多，通过融合后的预测结果越可信。

上述距离中，边为二元边，边的起始和结束，连接两个不同的顶点。边也可以是一元边，例如线性拟合问题，拟合的参数为一个顶点，多个采样点构成一元边，起始于参数顶点，结束于参数顶点，具体例子可以参考，视觉SLAM十四讲中的例子。

举例，对于二维SLAM问题，定义两种顶点:
机器人pose, $[x, y, \theta]$
路标坐标, $[x, y]$

运动方程，
$$f(x): \mathbbR^3 \to \mathbbR^3$$
观测方程，
$$h(x): \mathbbR^3 \to \mathbbR^2$$

pose to pose constraint:
$T_i = \Delta T_{ij} T_{j}$
某个pose处，激光测量，观测到一个空间点，顶点为一个2D pose: $[x, y, \theta]^T$ 和一个point: $[\lambda_x, \lambda_y]^T$, 观测数据是Polar坐标， 距离r与角度b
$$[r,b] = []$$





## 误差最小化least square error
对于待优化的变量，不管是位姿还是坐标，都是矢量，以向量的形式存储。其误差也是向量形式。但是最小二乘问题的目标函数，要求是一个标量。最直观的方式是取模(norm, 2范数)，也就是”平方“。矩阵形式为$e^Te$。同时为了表示对于个误差分量都的重视程度(精确度的信任度)不一样，还是用一个信息矩阵$\Omega$来进行不同的加权，总体的目标函数写成：
\begin{equation}
\min\limits_{x} \sum\limits_{k = 1}^n {{e_k}{{\left( {{x_k},{z_k}} \right)}^T}{\Omega _k}{e_k}\left( {{x_k},{z_k}} \right)}
\end{equation}

### 核函数 robust kernel function
在图中，可能会存在错误的边，对应最小二成中某一误差项过于的大，或者根本不合理。类似于观测中的outlier。因为算法目标是整体误差结果最小化，这会导致整体的结果出现偏移。如何有效的剔除outlier，或者最小化它的影响，是算法稳定的一大目标。
核函数的存在就是限制误差的增长。把传统的误差二范数度量，替换成一个在误差大的情况下，增长没有那么快的函数，同时，还必须保证自身的光滑可导行。

## 误差信息矩阵，系统信息矩阵
边信息矩阵$\Omega$，协方差矩阵的逆，最小二乘的权重，相关性越高，协方差越大，该误差权重越小。如果协方差越小，表示这次测量(边，constraint)越准，越值得相信。

信息矩阵有如下性质：

1, 对称矩阵 symmetric matrix
2, 对角线上元素为方差，如果各个误差间独立，那么为对角阵。对角阵元素大小表示误差的权重。

举例：$\Omega_{ij}代表i顶点与j顶点之间误差变量的协方差矩阵。如果一个边的对应的误差参数是$[\Delta x,\Delta y,\Delta \theta]^T$，
那么对应的协方差矩阵$\Omega_{ij} \in
\mathbbR^{3x3}$，因为是对称矩阵的缘故，只需要6个变量来存储:
$(inf_{xx}, inf_{xy}, inf_{x\theta}, inf_{yy}, inf_{y\theta}, inf_{\theta\theta})$

$e_{ij}(X_i, X_j) \in \mathbb R^{3x1}$, 

系统信息矩阵H

### full SLAM H的求解
### online SLAM H的维护更新

##矩阵形式的理解
最后落实到代码中，需要切实的理解数学中矩阵运算的具体分解步骤



## 相关博文
非常感谢相关博主无私的分享他们的理解！
[graph slam tutorial ：从推导到应用2]: (https://blog.csdn.net/heyijia0327/article/details/47731631)
[graph slam tutorial ：从推导到应用3]: (https://blog.csdn.net/heyijia0327/article/details/47428553)
[深入理解图优化与g2o：图优化篇]: (https://www.cnblogs.com/gaoxiang12/p/5244828.html)

## 从信息矩阵的方式去理解
在概率机器人一书中，推导方式是从信息滤波器角度推导的information filter,
而不是从最小二乘。

在信息矩阵的概念下，GraphSLAM只需要维护information matrix
$\Omega$与信息向量$\xi$，状态结果，也就是期望值，可以通过$\mu = {\Omega}^{-1} \xi$
计算得到。同时，可以对信息矩阵，信息向量尽心消元操作，使的其只包含pose信息。
然后先求得所有位姿信息，然后根据路标与相应的观测到次路标的位姿节点，求解路标信息，
得到地图信息。
