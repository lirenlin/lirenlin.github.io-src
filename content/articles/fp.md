Title: floating point
Date: Wed 23 Jan 17:16:15 CET 2019
Category: Programming
Tags: Programming

# Floating point
In computing, floating-point arithmetic (FP) is arithmetic using formulaic
representation of real numbers as an approximation so as to support a trade-off
between range and precision. For this reason, floating-point computation is
often found in systems which include very small and very large real numbers,
which require fast processing times. A number is, in general, represented
approximately to a fixed number of significant digits (the significand)
and scaled using an exponent in some fixed base; the base for the scaling
is normally two, ten, or sixteen. A number that can be represented exactly
is of the following form:
$$significand \times base^{exponent}$$

The term floating point refers to the fact that a number's radix point (decimal
point, or, more commonly in computers, binary point) can "float"; that is, it
can be placed anywhere relative to the significant digits of the number. This
position is indicated as the exponent component, and thus the floating-point
representation can be thought of as a kind of scientific notation.

* IEEE 16-bit binary float  
1 sign bit: s  
5 bit for exponent: u.
11 bits for significand: m, (one bit is implicit, 10 bits are explicitly stored.)
bias: 15


* IEEE 32-bit binary float  
1 sign bit: s  
8 bit for exponent: u  
24 bits for significand: m, (one bit is implicit, 23 bits are explicitly
			     stored.)
bias: 127

* IEEE 64-bit binary float  
1 sign bit: s  
11 for exponent: u  
53 bits for significand: m, (one bit is implicit, 52 bit are explicitly stored)
bias: 1023  

* IEEE 128-bit binary float  
1 sign bit: s  
15 for exponent: u  
113 bits for significand: m, (one bit is implicit, 112 bit are explicitly stored)
bias: 16383  

Some combinations of exponent and significant pattern are preserved for
specially number, e.g. 0, infinity, NaN.
\begin{align*}
e &= u - bias\\
significant &= 1(implicit) + m_1*2^{-1} + m_2*2^{-2} + ... m_m2^{-m}\\
val &= significant * 2 ^ {e}\\
\end{align*}

For example, for number 216:
```python
>>> import numpy as np
>>> float32_mem = np.float32(216).view(np.uint32)
>>> print float32_mem
1129840640
>>> bin(float32_mem)
'0b1000011010110000000000000000000'
#sign bit(31-bit): 0  
#exponent bit pattern(30-23bit): 0b10000110 (134)
#significand bit pattern(22-0bit): 0b10110000000000000000000
>>> e = 0b10000110 -127
>>> e
7
>>> significant = 1.0 + 2**-1 + 2**-3 + 2**-4
>>> significant
1.6875
>>> significant*2**e
216.0
```
Another example with rounding error:
```python
>>> float32_mem = np.float32(16777216).view(np.uint32)
>>> bin(float32_mem)
'0b1001011100000000000000000000000'
>>> e = 0b10010111 - 127
>>> significant = 1.0
>>> significant * 2**e
16777216.0
>>> float32_mem = np.float32(16777217).view(np.uint32)
>>> bin(float32_mem)
'0b1001011100000000000000000000000'
>>> e = 0b10010111 - 127
>>> significant = 1.0
>>> significant * 2**e
16777216.0
>>> significant = 1.0 + 2**-23
>>> significant * 2**e
16777218.0
>>> e
24
```

# ULP, unit in th last place
given a normalized representation in float point
$$d_1.d_2...d_p \times \beta^e$$
$d_1$ is not zero. the ULP value is defined as:
$$ulp(e, p) \to \beta^{e-(p-1)}$$
For example:
$$1.625 * 10^{-4}; \; \beta=10, e = -4, p = 4$$
$$ulp(10, 3) = 1 * 10^{-(p-1)} * 10^e = 10^{e-(p-1)} = 10^{-7}$$

In general, if the floating-point number $d.d...d ×\beta^{e}$ is used to represent z,
then it is in error by $|d.d...d - (z/\beta^{e})|\beta^{p-1}$ units in the last place


#[What Every Computer Scientist Should Know About Floating-Point Arithmetic](https://docs.oracle.com/cd/E19957-01/806-3568/ncg_goldberg.html)
