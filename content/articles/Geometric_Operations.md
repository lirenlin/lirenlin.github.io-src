Title: Geometric Operations
Date: Sat 26 Jan 17:49:37 CET 2019
Category: Math
Tags: Math

# Translation

# Rotation

# Affine transformation
线性变换+平移, 6 DOF

# Rigid transformation (Euclidean transform, SE(3))
Any Euclidean transformation is an affine transformation. But not the other way
around, for example, Reflections, Shear transformation.

6 Degrees Of Freedom
Transformation matrix = rotation + translation.

# 仿射函数与线性函数区别
> A linear function fixes the origin, whereas an affine function need not do so.
An affine function is the composition of a linear function with a translation,
so while the linear part fixes the origin, the translation can map it
somewhere else.

> Linear functions between vector spaces preserve the vector space structure
(so in particular they must fix the origin). While affine functions don't
preserve the origin, they do preserve some of the other geometry of the
space, such as the collection of straight lines.

> If you choose bases for vector spaces V
and W of dimensions m and n respectively, and consider functions f:V→W, then
f is linear if f(v)=Av for some n×m matrix A and f is affine if f(v)=Av+b
for some matrix A and vector b, where coordinate representations are used
with respect to the bases chosen.
