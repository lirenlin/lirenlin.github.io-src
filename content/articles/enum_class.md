Title: c++ enum class -- scoped and strongly typed enums
Date: Sun 18 Aug 16:45:44 CEST 2019
Category: c++
Tags: c++

## enum class
* enumerator names are local to the enum
* their values do not implicitly convert to other types
* the underlying type of an enum can be specified.

## plain enum
* enumerator names are in the same scope as the enum, causing name clashes.
* their values implicitly convert to intergers and other types
* the underlying type of an enum cannot be specified.

## enum and string mapping
Most of the time, we want a mapping between enum and string. So that we could
print some useful message. The most straight-forward way is to have a function
with switch statement inside. For each enumerators, return different
descriptive string. A mapping data structure could also be used for this
purpose.

To save some typing work, one could use macros/pre-processor to help with
code-generation.

Depending on how the string need to be, there are two cases:

* enum names themselves as strings
  There are various third-party code to do this. To list a few:

    * [better enum](https://github.com/aantron/better-enums)

    better enum is using macro to help with code generation. A struct is used
    to wrap all the functions. Conversion operator is defined so that, the
    struct could be used as a normal enumerator in swith/comparison statements

    * [magic_enum](https://github.com/Neargye/magic_enum)

    magic_enum is taking advantage of **\_\_PRETTY_FUNCTION\_\_** compiler magic
    constant to generate string from enumerators.

    This reuqires certain compiler support. gcc >= 9, clang/llvm >= 5.

        ```c++
        enum class Color {RED, GREEN, BLUE};
        //the string returned by this function contains the enumerator v's string representation.
        // E is enum type, v is a enumerator of E enum.
        template<typename E, E v>
        std::string getEnumName() { return __PRETTY_FUNCTION__;}
        std::cout << getEnumName<Color, Color::GREEN>() << std::endl;
        //The output will look like:
        //std::string getNameImpl() [E =Color, v = Color::BLUE]
        ```

* Other user supplied string mapping

## Reference
[Bjarne Stroustrup's C++11 FAQ](http://www.stroustrup.com/C++11FAQ.html#enum)

[stackoverflow: Why is enum class preferred over plain enum?](https://stackoverflow.com/questions/18335861/why-is-enum-class-preferred-over-plain-enum)

