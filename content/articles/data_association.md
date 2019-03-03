Title: Data Association
Date: Tue 19 Feb 19:01:19 CET 2019
Category: SLAM
Tags: SLAM


## Mahalanobis distance

## Random sample consensus (RANSAC)
Random sample consensus (RANSAC) is an iterative method to estimate parameters
of a mathematical model from a set of observed data that contains outliers,
when outliers are to be accorded no influence on the values of the estimates.
Therefore, it also can be interpreted as an outlier detection method.[1] It is
a non-deterministic algorithm in the sense that it produces a reasonable result
only with a certain probability, with this probability increasing as more
iterations are allowed.

直观上，可以一定程度上的排除outliers。有两个应用

1. 系统参数的估计/拟合。给定一组带有噪声的数据与一个系统模型，通过数据来确定系统
模型的参数。因为数据中外点，会导致拟合的系统出现偏移。所以去除外点对于正确的系统
估计很重要。
同时，外点不同于噪点，噪点可以通过统计的方式消除，当然还需要数据量足够大才行。
2. 图像特征匹配中，消除误匹配点。
在图像特征匹配以后，会得到很多对特征匹配。但是其中有一些匹配是误匹配，如果不加挑选，
使用所有的匹配对进行运动的计算，可能会得到错误的运动数据(旋转，平移)。RANSAC可以用来
消除误匹配，然后使用剩下的匹配来估计运动。

上述过程类似，
1. 随机选取n个数据点
2. 根据一个给定模型，计算模型参数
3. 从原始数据集合中，根据上述求得模型，寻找其他的符合这个模型的数据点(在一定误差范围内)，
加入到一个集合里。称为内点集合
4. 如果总的内点个数大于M，则利用内点集合，重新估计模型参数，计算整体(使用所有数据点)误差。
跟上一次整体误差比较，如果误差更小，则更新误差，记录模型参数。
5. 跳转到步骤一，继续下一次迭代。直到迭代次数达到，或者整体误差小于一个预定值。

从上面步骤中看出，这个迭代过程，有很多参数需要设置。这也是RANSAC的一个缺点。



## Probabilistic data association filter

## ICP
通过迭代的方式，来解决data association与变换矩阵问题。

### point subset
* Use all points
* Uniform sub-sampling
* Random sampling
* Feature based sampling
* Normal-space sampling
### weighting the correspondences
### data association
* closet point
* normal shooting
* closest compatible point
* projection-based
### rejecting certain (outlier) point pairs

