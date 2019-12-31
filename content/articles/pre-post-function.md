Title: pre-post function in c++
Date: Sun 27 Oct 17:33:12 CET 2019
Category: c++
Tags: c++


# RAII
* constructor contains prefix-code
* destructor excutes postfix-code
* overload call operator () to contain the actual function call

This could only wrap the call once, not to every call into the object.
And the destructor is only executed at the end of block.
Check the next method for a more generic wrapper.


# generic wrapper:
overloading the '->' operator of a template class.
prefix code in '->' operator before returing the pointer.
postfix code in deconstructor

From cppreference:
> If a user-defined operator-> is provided, the operator-> is called again on
the value that it returns, recursively, until an operator-> is reached that
returns a plain pointer. After that, built-in semantics are applied to that pointer.

[Wrapping C++Member Function Calls]:http://www.stroustrup.com/wrapper.pdf

## ownership
