Title: 卡尔曼滤波，最大似然，最小二乘
Date: Mon 28 Jan 23:33:07 CET 2019
Category: Math
Tags: Math

最小二乘估计：不考虑数据的统计特性，如期望，方差等，直接用最小二乘法得到最优估计。
最小二乘估计只保证测量值与估计值的平方和最小，不保证估计误差的方差最小。最小二乘估计不需要随机变量V的任何统计信息。


测量误差（测量）服从高斯分布的情况下， 最小二乘法等价于极大似然估计。(负对数)

卡尔曼误差高斯分布后验概率推导
http://www.cnblogs.com/ycwang16/p/5999034.html

卡尔曼最小均方差推导
卡尔曼滤波就是递推最小二乘法的一种特殊情况，卡尔曼滤波也是去通过最小化方差来求得最优的估计值。
[卡尔曼滤波 -- 从推导到应用]:(https://blog.csdn.net/heyijia0327/article/details/17487467)


[最大似然估计,最小二乘估计,卡尔曼滤波,三者的相互关系](https://blog.csdn.net/ethan_guo/article/details/80568254)
[SLAM学习笔记2：Kalman Filter(卡尔曼滤波) 与Least Square(最小二乘法) 的比较](https://blog.csdn.net/qinruiyan/article/details/50793114)

