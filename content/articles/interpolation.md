Title: Interpolation
Date: Thu  3 Jan 23:32:10 CET 2019
Category: Math
Tags: Math

In the mathematical field of numerical analysis, interpolation is a method of
constructing new data points within the range of a discrete set of known data
points.

In engineering and science, one often has a number of data points, obtained by
sampling or experimentation, which represent the values of a function for a
limited number of values of the independent variable. It is often required to
interpolate, i.e., estimate the value of that function for an intermediate
value of the independent variable.

* linear interpolation.
Linear interpolation is quick and easy, but
	* It is not very precise.
	* The interpolant is not differentiable at the point $x_k$.
* Polynomial interpolation
Overcomes most of the problems of linear interpolation. (error, differentiable)
However, polynomial interpolation also has some disadvantages.
	* Calculating the interpolating polynomial is computationally expensive
	compared to linear interpolation.
	* polynomial interpolation may exhibit oscillatory artifacts,
  especially at the end points (see Runge's phenomenon).

* Spline interpolation
	* smaller error than linear interpolation
	* interpolant is smoother.
	* the interpolant is easier to evaluate than the high-degree polynomials used
	in polynomial interpolation
	* However, the global nature of the basis functions leads to
	ill-conditioning. This is completely mitigated by using splines of compact
	support, such as are implemented in Boost.Math and discussed in Kress.

A simple (well behaved) differentiable interpolation is the Cubic
Hermite Spline

[Wiki: Interpolation](https://en.wikipedia.org/wiki/Interpolation#Polynomial_interpolation)

