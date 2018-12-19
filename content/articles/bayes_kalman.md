Title: Bayes and Kalman Filter
Date: 2018-12-18
Category: Math
Tags: Math, SLAM

SLAM位姿与地图估计问题有两种方式，一种是滤波，一种是优化.<br/>
暂时搜集到的一些信息，没有自己整理

Bayes Filter推导(基于Bayes公式与Markov assumption)<br/>
<img src="images/bayes-1.png" alt="Bayes" title="bayes" style="width:50%"/>

第一步用到的Bayes公式：
$$P(x|y,z) = \frac{P(y|x,z)\cdot p(x|z)}{p(y|z)}$$
由此得出，贝叶斯滤波器分为两步：<br/>
<img src="images/bayes-3.jpeg" alt="Bayes" title="bayes" style="width:50%"/>

在此式中$\eta$未进一步说明，概率机器人一书中，被称之为归一化因子，具体表现形式如下：
$$\frac{1}{\eta} = \sum{p(z_t|x_t)\overline{bel}(x_t)dx_t}$$
因为最后$bel(x_t)$是一个概率，其所有$x_t$可能性概率的总和必须为１.

伪代码流程如下: <br/>
<img src="images/bayes-2.png" alt="Bayes" title="bayes" style="width:50%"/>

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
