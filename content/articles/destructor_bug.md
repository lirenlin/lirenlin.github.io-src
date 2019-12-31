Title: desctruction order
Date: Sat  9 Nov 12:28:35 CET 2019
Category: C++
Tags: C++

# A tricky bug
https://ibob.github.io/blog/2019/11/07/dont-use-unique_ptr-for-pimpl/


>
Order of destruction  
When an object goes out of scope or is deleted, the sequence of events in its complete destruction is as follows:  
1. The class's destructor is called, and the body of the destructor function is executed.  
2. Destructors for nonstatic member objects are called in the reverse order in which they appear in the class declaration. The optional member initialization list used in construction of these members does not affect the order of construction or destruction.  
3. Destructors for non-virtual base classes are called in the reverse order of declaration.  
4. Destructors for virtual base classes are called in the reverse order of declaration.  
[Mircrosoft: Destructors (C++)]


# Further read

https://isocpp.org/wiki/faq/dtors

https://docs.microsoft.com/en-us/cpp/cpp/destructors-cpp?view=vs-2019
