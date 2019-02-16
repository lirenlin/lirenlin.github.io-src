Title: Bayes and Kalman Filter
Date: 2018-12-18
Category: Math
Tags: Math, SLAM

SLAM位姿与地图估计问题有两种方式，一种是滤波，一种是优化.<br/>
暂时搜集到的一些信息，没有自己整理

Bayes Filter推导(<span style="color:red">基于Bayes公式与Markov assumption</span>)<br/>
<img src="images/bayes-1.png" alt="Bayes" title="bayes" style="width:50%"/>

第一步用到的Bayes公式：
$$P(x|y,z) = \frac{P(y|x,z)\cdot p(x|z)}{p(y|z)}$$
由此得出，贝叶斯滤波器分为两步：<br/>
1. 状态预测，基于状态转移模型：
$$\overline {bel} ({x_t}) = \int {p({x_t}|{u_t},{x_{t - 1}})} \;bel({x_{t - 1}})\;d{x_{t - 1}}$$
2. 状态更新，基于新的观测
$$bel({x_t}) = \;\eta \,p({z_t}|{x_t})\,\overline {bel} ({x_t})$$

在此式中$\eta$未进一步说明，概率机器人一书中，被称之为**归一化因子**，具体表现形式如下：
$$\frac{1}{\eta} = \sum{p(z_t|x_t)\overline{bel}(x_t)dx_t}$$
因为最后$bel(x_t)$是一个概率，其所有$x_t$可能性概率的总和必须为１.

伪代码流程如下: <br/>
<img src="images/bayes-2.png" alt="Bayes" title="bayes" style="width:50%"/>

<span style="color:red">
同时，我们注意，我们的目的是计算$x_t$的后验概率，如果$bel(x_t)$是任意分布，
我们需要在$x_t$的所有可能取值点上，计算该取值的概率，这在计算上是难于实现的。
</span>

相关资料的搜集:<br/>
[Bayes Filter by Cyrill Stachniss]({filename}/pdfs/slam02-bayes-filter-short.pdf)
<br/>
[Introduction to Mobile Robotics - Bayes Filter – Kalman Filter](http://ais.informatik.uni-freiburg.de/teaching/ss10/robotics/slides/10-kalman-filter.pdf)
<br/>
[SLAM中的EKF，UKF，PF原理简介](https://www.cnblogs.com/gaoxiang12/p/5560360.html)
<br/>
[SLAM笔记三——贝叶斯滤波器](https://blog.csdn.net/qq_30159351/article/details/53395515)
<br/>
[SLAM学习笔记2：Kalman Filter(卡尔曼滤波) 与Least Square(最小二乘法) 的比较](https://blog.csdn.net/qinruiyan/article/details/50793114)
<br/>
[细说贝叶斯滤波：Bayes filters](https://www.cnblogs.com/ycwang16/p/5995702.html)
<br/>
[细说Kalman滤波：The Kalman Filter](http://www.cnblogs.com/ycwang16/p/5999034.html)
