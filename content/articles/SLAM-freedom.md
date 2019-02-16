Title: 位姿图优化空间平移问题
Date: Sat 16 Feb 20:20:10 CET 2019
Category: SLAM
Tags: SLAM

A Tutorial on Graph-Based SLAM[^1]
中有提到一个细节，

>
Note that the error of a constraint $e_{ij}$ depends only on the relative position
of the connected pose $x_i$ and $x_j$.  Accordingly, the error $F(x)$ of a
particular configuration of the pose sxis invariant under a rigid transformation
of all the poses. This results in Eq. 15 being under determined. To numerically
solve this system it is therefore common practiceto constrain one of the
increments $\Delta x_k$ to be zero. This can bedone by adding the identity matrix to
thekthdiagonal block $H[kk]$.  Without loss of generality in Algorithm 1 we
fix the first node $x1$. An alternative way to fix a particular node
of the pose-graph consists in suppressing the kth block row and the kth block column
of the linear system in Eq. 15.

$e_{ij}$约束的误差，只取决于$x_i$与$x_j$的相对位置。如果所有的位姿点，统一进行一个刚体
变换，那么目标error function是不变的，系统欠定，有无数解。

同样更广泛的问题在Visual SLAM Tutorial: Bundle Adjustment[^2]中，有专门一章节来描述。


[^1]: [A Tutorial on Graph-Based SLAM](http://www2.informatik.uni-freiburg.de/~stachnis/pdf/grisetti10titsmag.pdf)
[^2]: [Visual SLAM Tutorial: Bundle Adjustment]({filename}/pdfs/Visual_SLAM_Tutorial_Bundle_Adjustment.pdf)
