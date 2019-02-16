Title: ICP
Date: Thu  7 Feb 17:54:55 CET 2019
Category: Math
Tags: Math

Iterative Closest Point Algorithm主要由两部分组成[^1]

* Data Association
	* Closest-Point Matching  
Kd-trees
	* Normal Shooting  
Slightly better convergence results than closest point for smooth structures,
worse for noisy or complex structures
* Error Metric:
	* point to point  
  SVD解法
	* point to plane[^3]  
Each iteratrion generally slower than the point-to-point versin, however, often
significantly better convergence rates.  
solved using standard linear least-squares problem


## 基于k-d tree的ICP算法计算分析
使用k-d tree来加速整个过程的计算。总体计算花销分为两方面:

* <span style="color:red"> 从参考点云建立k-d树需要花销 </span>
* <span style="color:red"> k-d tree 查找的花销，其中主要是三个步骤，DFS查找，
ball-within-bounds test和backtracking. </span>
* <span style="color:red"> 同时，因为使用了kd-tree数据结构，那么tree的平衡性，
会对整个查找复杂度有很大影响 </span>

在SLAM中，得到t时刻与t+1时刻的两幅环境的稀疏扫描点云，需要point
registreation来计算两个时刻间，机器人的位姿(pose)变换(rotation + translation)。
这当中包含一次k-d tree的简历，与许多次的ICP迭代，每次迭代，都需要对每一个query
point进行k-d tree的查找。

有很多的优化方法，让r-d tree的建立，查找操作都更加快速。这些优化对于点云的拓扑结构
有一些假设。这些假设，在机器人应用场景下，不一定成立。大多时候，场景通过机器人的
传感器稀疏采样的。


### cached k-d tree search for ICP algorithms[^2]
在论文中，作者有如下评论

> <span style="color:red">
However, these state of the art ICP variants all assume that the input data is
given as a mesh.  In many application scenarios a mesh is not available, e.g.,
3D data in robotics. Here, measurements contain in addition to Gaussian noise so
called salt-and-pepper noise. Furthermore, in robotics the scenes are often
sparsely sampled by the sensor. For these two reasons, simple meshing methods
based on the topology of the acquired points cannot be applied and roboticists
stick to using the raw point clouds. In this case the point-to-point metric,
cf. Eq. (1), and closest point search have to be used.
</span>

所以传统的point-to-point error metric, k-d tree based closed point
search还是主流。目前我还没有阅读其他论文，所以无法评论作者观点是否正确。但是如果
真的这样，就只能在机器人场景下，，使用比较传统的方式。但是，r-d
tree的构建，查找还是可以利用硬件特性，例如GPU进行加速。

在这篇论文中，作者改进了backtracking的思路，减少DFS搜索次数，同时使得backtracking
操作大致constant time。这是利用ICP的迭代算法特性，因为如果整个过程收敛，越到后面，
变换矩阵会越来越小，通过记录上一个iteration，查询点在r-d
tree中大致的位置，可以在当前iteration中大致估计，也会在差不多的位置。所以，不同于从
root开始重新查找一遍，这次从上一次的leaf node开始，反向查找。

作者给出了性能比较，整体性能提升很明显。在这里，bucket size对性能也有影响。
通常对于k-d tree的讲解资料中，bucket size是1。在作者给出的性能对比中，cached
kd-tree在bucket size为1的时候提升最大。同时值得注意的是，bucket size
为1的时候，整体性能是最差的。所以为了寻求绝对性能的最大，还是要尝试不同的bucket
size。

在文中，作者同时提到

> <span style="color:red">
The overall performance of the ICP algorithm depends
both on the search time and on the construction time
of the tree. However, the construction time of the trees
seems to be negligible.
</span>

在他的测量中，kd-tree的建立花销对整体性能影响不大，这也需要自己实际去测量。

cached kd-tree需要一块内存在缓存上一迭代的结构，同时因为需要回溯的缘故，
每一个树节点需要保存一个父节点的指针。所以它会有额外的存储花销$O(N_d) +
O(N_m)$, $N_m$为reference data cloud point点数，$N_d$为待匹配点云点数。

### kd-tree construction optimization
普通情况下，需要寻找以当前划分坐标轴为衡量标准的所有点的中位数(median)，在naive
的算法里, median-finding algorithm复杂度为$O(n)$，使用排序的方法的话，
可以优化到$nO(log\;n)$

具体可参考[wiki, ICP Complexity](https://en.wikipedia.org/wiki/K-d_tree#Complexity)


[^1]: http://ais.informatik.uni-freiburg.de/teaching/ss10/robotics/slides/17-icp.pdf
[^2]: [Cached k-d tree search for ICP algorithms]({filename}/pdfs/Cachedk-d_tree_search_for_ICP_algorithms.pdf)
[^3]: https://www.comp.nus.edu.sg/~lowkl/publications/lowk_point-to-plane_icp_techrep.pdf

