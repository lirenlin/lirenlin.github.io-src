Title: SLAM
Date: Tue 29 Jan 16:27:32 CET 2019
Category: SLAM
Tags: SLAM

## 纯激光SLAM地图构建
如果平台只有激光测距的传感器，那个这个系统只有观测方程，没有运动方程。

在卡尔曼滤波中，步骤分为预测与更新，没有了运动方程，这里只能有一步。由于没有额外
的信息来消除误差，在运动/观测过程中的误差不会被消除，只会一直积累。

这需要依赖后端的图优化来一次性优化所有地图的信息，这里回环检测就非常重要，它添加额外的非常
重要的信息。也就是在图优化的术语中，添加了一个非常强的约束。

对于运动的估计，利用点云匹配的方法求出，也就是位移与旋转。常用的方法有ICP。在这里，
算法的稳定性尤为重要，因为这是唯一的估计运动的来源。由于，相邻的测量数据里只有部
分信息重合，需要避免误匹配。同时，计算量会很大，效率很重要。

scan to scan
scan to map
map to map


## landmark extraction from laser scan
也称作环境feature extraction?

* Spike landmarks, 对于环境中类似于脱离背景的人，因为其筛选标准，会错误判断为路标
* RANSAC, use line extraction, 对于环境中移动的人，有一定的稳定特性。但是对于块状移动物体，例如汽车，肯能也会错误的识别为路标
* scan mathing, 不提取特征，直接比较相邻时刻的laser scans, 计算量问题，稳定性问题，data point reduce, data align问题。后续有看到feature-based laser scan mathing 文章。

## KF-SLAM, online SLAM
<figure>
<img src="images/slam04_ekf_state.png" alt="EKF state" title="EKF state" style="max-width:80%;max-height:80%"/>
<figcaption> Figure. EKF state representation[^1] </figcaption>
</figure>
<figure>
<img src="images/slam08_kf_complexity.png" alt="EKF complexity" title="EKF complexity" style="max-width:80%;max-height:80%"/>
<figcaption> Figure. EKF complexity[^2] </figcaption>
</figure>
因为图1中状态的表示与路标数成比例，协方差矩阵(信息矩阵)的大小是路标数量的二阶形式。在卡尔曼滤波过程中，一直需要维护更新这个矩阵。
### EKF
### UKF
### SEIF


## 拥有反馈的SLAM系统
在这个系统中，有多种传感器，融合所有传感器的信(sensor fusion)，可以修正一定的误差


## Online SLAM vs Full SLAM

在没有回环检测的时候，卡尔曼滤波与图优化的优劣，strip状的路径
卡尔曼滤波计算更小，数据存储越小？

* 前端
    1. 特征点提取
    2. 特征匹配，计算相对运动矩阵，估计位姿，估计路标坐标
    3. 回环检测
* 后端
    4. 优化，更新位姿，路标
    5. parameterization: 优化方法求导，四元数
    iterative non-linear optimization: LM, Gauss-Newton etc.
    solve symstem of linear euqation: 计算
    matrix decomposition: 计算
    matrix sparseness: 问题的结构，优化计算
    numeric stability(condition number):
    Marginalization: 消原，或者局部更新，window
    outlier: 

[^1]: http://ais.informatik.uni-freiburg.de/teaching/ws12/mapping/pdf/slam04-ekf-slam.pdf
[^2]: http://ais.informatik.uni-freiburg.de/teaching/ws12/mapping/pdf/slam08-kf-wrapup.pdf
