Title: Robust regression
Date: Fri  1 Feb 01:06:33 CET 2019
Category: Math
Tags: Math

最小二乘法对于outlier比较敏感

对于高斯噪声，最大似然等同于最小二乘
https://www.jianshu.com/p/d0ea25071c57

So for least squares to have a useful statistical interpretation, the Wi should 
be chosen to approximate the inverse measurement covariance of z i.
Even for non-Gaussian noise with this mean and covariance, the Gauss-Markov
theorem [37, 11] states that if the models zi (x) are linear, least squares
gives the Best Linear Unbiased Estimator (BLUE), where ‘best’ means minimum
variance.

Least square with covariance as weight matrix??

## robust regression
loss function
