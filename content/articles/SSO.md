Title: Short/Small string Optimization
Date: Sun 27 Oct 19:21:56 CET 2019
Category: Programming
Tags: Programming

small strings are embedded in the body of the string class rather than using a
separately allocated buffer.

1. avoid heap allocation.
2. avoid access indirection

## Ref
[sso](https://stackoverflow.com/questions/27631065/why-does-libcs-implementation-of-stdstring-take-up-3x-memory-as-libstdc/28003328#28003328)

[stackoverflow](https://stackoverflow.com/questions/10315041/meaning-of-acronym-sso-in-the-context-of-stdstring)


