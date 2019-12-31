Title: Copy constructor VS. Mov constructor
Date: Sun 10 Nov 14:11:43 CET 2019
Category: C++
Tags: C++

# Overload resolution

> If both copy and move constructors are provided and no other constructors are viable, overload resolution selects the move constructor if the argument is an rvalue of the same type (an xvalue such as the result of std::move or a prvalue such as a nameless temporary (until C++17)), and selects the copy constructor if the argument is an lvalue (named object or a function/operator returning lvalue reference).

## Special member functions
<figure>
<img src="images/c++_special_member.png" alt="c++ special member functions" title="special member functions" style="max-width:100%;max-height=100%"/>
<figcaption> Fig. C++ special member functions </figcaption>
</figure>
