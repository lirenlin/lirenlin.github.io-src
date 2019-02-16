Title: BA vs Graph SLAM
Date: Fri 15 Feb 13:05:07 CET 2019
Category: SLAM
Tags: SLAM

state vector
error function

1. parameterization for the state vector
	* minimum parameterization, 对于分量是分别计算的，在有冗余的时候，例如旋转矩阵R，他们之间的约束没有表示出来，会求得不合理的组合
	但是对于 minimum parameterization，可能不存在欧式空间的加法。不连续可导。
	* Extended parameterization

$[x, y, \theta]$ or $T \to \mathbb SE(3)$

It is a well known thing that 3D rotations can be parameterized with a
rotation matrix R. A rotation matrix, however has 9 numbers to represent 3 angles. If we would use
the rotation matrices as parameters in our optimization mechanism we would find non-valid solutions,
since the orthogonality constraint is not enforced. Thus, it seems there is no alternative than carrying
on the optimization by using a minimal representation, for instance Euler angles. But we just said that
Euler angles suffer of singularities. Lucky us, the rotations are a manifold. That is, they admit a local
parameterization which is homeomorphic to the vector space Rn . To explain this sentence, think to a
generic rotation R(ρ, θ, ψ). We can easily define a mapping between rotation matrices and Euler angles,
and vice versa:

2. if the state variable do not live in Euclidean space
	* define a parameterization for the increment
	* define $\boxplus$ operator.

local parameterization of the increments $\Delta X$ if X is not in E



iteration state vector update
$X = X \boxplus \Delta X$


