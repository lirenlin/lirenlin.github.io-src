Title: Header-only library
Date: Sat  9 Feb 15:51:09 CET 2019
Category: Programming
Tags: Programming

## Function definition in the header
The preprocessor will literally copy the content of header into the including
file. The `ifdef` guard makes sure, for a given file, the same header file is
only included once.

It is fine that a function is defined in the header. The compiler(in this
sense, it doesn't include the assembler or linker part) won't complains any
thing. The C source file will be compiled into an object with symbol
information. When it comes to the linking stage, if there are multiple object
files have the same symbol definition in their symbol table, the linker will
throw error, something like "multiple definition".

One way the circumvent this is to add `inline` attribute to every function
definition in the header. So that no symbol will be created. The other possible
solution is to add `static` attribute to the function definition.

## Function definition inside class definition
A member function that is defined inside its class member list is called an
inline member function.

Once can also declare the function as `inline`, and define it outside of class
definition.

`inline` attribute is merely a hint to the compiler. So it won't always give
the same effect as macro.

> The main (only?) use for the inline keyword nowadays it to allow functions to
be defined in the header and not generate multiple definition link errors
(which has nothing to do with inlining really).

## Template class
template libs must be provided as head-only form. The compiler need to know the
the parameter types as well as the library code at the time.

## Advantage/Disadvantage of head-only library
In theory, the compiler could do better optimization when the definition is
visible to it. But nowadays, the compiler could do optimization across compilation
unit. And because of other complications like linker optimization, hardware
features, the benefit is not always observable.

It is best to measure the code size and performance change with specific use
case. And code maintainability is also an import aspect to consider.

## Link
https://stackoverflow.com/questions/16679709/defining-member-functions-inside-the-class-definition

https://en.wikipedia.org/wiki/Header-only

https://softwareengineering.stackexchange.com/questions/305618/are-header-only-libraries-more-efficient
