Title: 范数Norm
Date: Tue 15 Jan 15:47:30 CET 2019
Category: Math
Tags: Math

# 向量范数(norm)
From wiki:
> In linear algebra, functional analysis, and related areas of mathematics,
> a norm is a function that assigns a strictly positive length or size to
> each vector in a vector space—except for the zero vector, which is
> assigned a length of zero.
# 矩阵范数
From wiki:
> In mathematics, a matrix norm is a vector norm in a vector space whose elements
> (vectors) are matrices (of given dimensions).

可以从函数、几何与矩阵的角度去理解范数。

我们都知道，函数与几何图形往往是有对应关系的，这个很好想象，特别是在三维以下的空间内，函数是几何图像的数学概括，而几何图像是函数的高度形象化，比如一个函数对应几何空间上若干点组成的图形。
但当函数与几何超出三维空间时，就难以获得较好的想象，于是就有了映射的概念，映射表达的就是一个集合通过某种关系转为另外一个集合。通常数学书是先说映射，然后再讨论函数，这是因为函数是映射的一个特例。
为了更好的在数学上表达这种映射关系，（这里特指线性关系）于是就引进了矩阵。这里的矩阵就是表征上述空间映射的线性关系。而通过向量来表示上述映射中所说的这个集合，而我们通常所说的基，就是这个集合的最一般关系。于是，我们可以这样理解，一个集合（向量），通过一种映射关系（矩阵），得到另外一个集合（另外一个向量）。
那么向量的范数表示这个原有集合的大小。
矩阵的范数表示这个变化过程的大小的一个度量。
简单说：0范数表示向量中非零元素的个数（即为其稀疏度）。1范数表示为，绝对值之和。而2范数则指模。

具体向量范数与矩阵范数参见
[知乎：0 范数、1 范数、2 范数有什么区别？](https://www.zhihu.com/question/20473040)  
[mathworld: Vector Norm](http://mathworld.wolfram.com/VectorNorm.html)
