Title: SVD
Date: Thu 10 Jan 16:21:16 CET 2019
Category: Math
Tags: Math

# 特征值分解
要求: 方阵
线性代数中，特征分解（Eigendecomposition），又称谱分解（Spectral decomposition）
是将矩阵分解为由其特征值和特征向量表示的矩阵之积的方法。
需要注意只有对可对角化矩阵才可以施以特征分解.

令 A 是一个 N×N 的方阵，且有 N 个线性无关的特征向量 $q_{i}\,\,(i=1,\dots ,N)$。
这样， A 可以被分解为
$$\mathbf {A} =\mathbf {Q} \mathbf {\Lambda } \mathbf {Q} ^{-1}$$
其中 Q 是N×N方阵，且其第 i列为 A 的特征向量 $q_{i}$。 Λ 是对角矩阵，
其对角线上的元素为对应的特征值，也即 $\Lambda_{ii}=\lambda_{i}$。这里需要注意
只有可对角化矩阵才可以作特征分解。 比如
$$\begin{bmatrix}1&1\\0&1\\\end{bmatrix}$$
不能被对角化，也就不能特征分解。

一般来说，特征向量 $ q_{i}\,\,(i=1,\dots ,N)$ 一般被单位化（但这不是必须的）。
未被单位化的特征向量组 $ v_{i}\,\,(i=1,\dots ,N)$, 也可以作为 Q 的列向量。
这一事实可以这样理解： Q 中向量的长度都被$Q^{−1}$抵消了。

# 谱分解
要求: 正规矩阵

# 奇异值分解Singular Value Decomposition
## 定义
奇异值分解是一个能适用于任意的矩阵的一种分解的方法
SVD 分解说的是：假设 M 是一个 m×n 的矩阵，其中的元素全部属于数域 𝕂
（实数域 ℝ 或复数域 ℂ）。那么，存在 m×m 的酉矩阵 U 和 n×n 的酉矩阵 V
使得
$$\mathbf M = \mathbf U\mathbf\Sigma\mathbf V^{\mathsf H}$$
其中 $\Sigma$ 是 m×n 的非负实数对角矩阵；并且$\Sigma$ 对角线上的元素
$\Sigma_{i,i}$ 是 M 的奇异值。
一般来说，我们偏好将这些奇异值按从大到小的顺序排列，这样一来 Σ 就由 M 唯一确定了。
另一方面，因为 U 和 V 都是酉矩阵，所以 U 和 V 的列向量分别张成 𝕂m 和 𝕂n 的一组标
准正交基。我们将 U 的列向量记作 u⃗ i,1⩽i⩽m；将 V 的列向量记作 v⃗ j,1⩽j⩽n；同时，
将 Σ 对角线上的第 i 个元素记作 σk,1⩽k⩽min(m,n)。那么，SVD 分解实际可以将矩阵 M
写作一个求和形式
$$\mathbf M = \sum_{i = 1}^{\min(m, n)}\Sigma_i\vec u_i\vec v_i^{\mathsf T}$$

## SVD计算

## SVD分解几何解释
$$\mathbf M = \mathbf U\mathbf\Sigma\mathbf V^{\mathsf H}$$
旋转, 缩放, 旋转

U 和 V 都是旋转矩阵 (标准正交基)

## SVD应用
SVD分解至少有两方面作用：

* 分析了解原矩阵的主要特征和携带的信息（取若干最大的奇异值），这引出了主成分分析（PCA）；
* 丢弃忽略原矩阵的次要特征和携带的次要信息（丢弃若干较小的奇异值），这引出了信息有损压缩、矩阵低秩近似等话题。

## 奇异向量的现实意义
SVD也可以得到协方差矩阵XTX最大的d个特征向量张成的矩阵，但是SVD有个好处，有一些SVD的实现算法可以不求先求出协方差矩阵XTX，也能求出我们的右奇异矩阵V

# 参考整理来源
https://www.zhihu.com/question/22237507  
https://liam.page/2017/11/22/SVD-for-Human-Beings/  
https://www.cnblogs.com/pinard/p/6251584.html  
