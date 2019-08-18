Title: c++ term
Date: Sun 28 Jul 12:43:31 CEST 2019
Category: c++
Tags: c++

closure
free varialbe
first order function

callable object
  * function object, functor
  A function object (or functor) is simply any object of a class that provides at least one definition for operator() What this means is that if you then declare an object f of the class in which this operator() is defined you can subsequently use that object f just like you would use an "ordinary" function.
  * lambda expression
  * bind expression
  * free functions
  * member functions

STL function objects
type erasure

# why lambda expression could be inlined?
https://stackoverflow.com/questions/13722426/why-can-lambdas-be-better-optimized-by-the-compiler-than-plain-functions

lambda expression are function object.
its type is passed to the a function template, which will results in a specific
version for this template type argument.

In this case, the compiler knows the type and implementation of function call operator. It has better chances to do some optimizations.



