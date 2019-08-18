Title: MLE & MAP
Date: 2018-12-18
Category: Math
Tags: Math, SLAM

MLE：最大似然概率 给定测量结果，系统模型，寻求系统模型参数让结果跟观测结果最贴近。

似然函数（也称作似然），是一个关于统计模型参数的函数。也就是这个函数中自变量是统计模型的参数。

对于观测结果 x ，在参数集合 θ 上的似然，就是在给定这些参数值的基础上，观察到的结果的概率 P(x|θ) 。
也就是说，似然是关于参数的函数，在参数给定的条件下，对于观察到的 x 的值的条件分布。

MAP:最大后验概率, 考虑到先验概率的存在 prior probability.
Bayes rule
$$P(\theta|x) = \frac{P(x|\theta) * p(\theta)}{p(x)}$$
$$P(x|y,z) = \frac{P(y|x,z)\cdot p(x|z)}{p(y|z)}$$

$$\hat{\theta} = \mathop{arg\max}_{\theta} P(\theta|x) \propto P(x|\theta) * p(\theta)$$
分母可以去掉，与求参数无关


已知观测结果，寻找参数，使得模型输出最符合观测。

[全概率公式](https://zh.wikipedia.org/wiki/%E5%85%A8%E6%A6%82%E7%8E%87%E5%85%AC%E5%BC%8F)

[最大似然估计 （MLE） 最大后验概率（MAP）](http://www.cnblogs.com/sylvanas2012/p/5058065.html)

[概率与似然](https://zhuanlan.zhihu.com/p/25768606)

[详解最大似然估计（MLE）、最大后验概率估计（MAP），以及贝叶斯公式的理解](https://blog.csdn.net/u011508640/article/details/72815981)
