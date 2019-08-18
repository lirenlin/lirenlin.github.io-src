Title: std::bind vs lambda
Date: Sat 27 Jul 21:00:09 CEST 2019
Category: c++
Tags: c++

# lambda vs std::bind
基本上是两个不同的用途，但是lambda可以实现std::bind的功能.
如果目的知识想去创造一个scope临时的函数，例如提供给STL的函数。lambda非诚使用这种使用场景。
1. 不需要单独的写一个函数，与使用逻辑分开。非常紧凑，没有context switch
2. lambda 可以inline，compiler可以做更多的优化


但是如果lambda只是capture variable，然后调用另一个外部函数的话，bind更加的简单直接。
"Simpler and clearer" is a matter of opinion. For simple binding cases, bind can take a lot less typing. bind also is focused solely on function binding, so if you see std::bind, you know what you're looking at. Whereas if you use a lambda, you have to look at the lambda implementation to be certain of what it does.

https://stackoverflow.com/questions/15598607/when-should-i-use-stdbind

但是注意，std::bind参数的传递只能通过copy, move。不能通过reference。这需要通过std::ref/std::cref

#
```
#include <iostream>
#include <functional>

class Data {
public:
  Data (int a, int b): _a(a), _b(b) {}
  // deleted copy constructor, std::bind will fail because of this. It cannot
  // make a copy for the binding arguments. Instead std::ref could be used to
  // pass remove the copy operation
  Data (const Data&) = delete;

  int getResult() const {return _a + _b;}
  void inc() {_a++;}

private:
  int _a;
  int _b;

  // declaration doesn't affected by class access specifier
  friend std::ostream& operator<<(std::ostream &os, const Data& data);
};

std::ostream& operator<<(std::ostream &os, const Data& data)
{
  return os << &data << " data object: " << data._a << " " << data._b;
}


int foo_cref (const Data& data) {
    return data.getResult();
}

int foo_ref (Data& data) {
    data.inc();
    return data.getResult();
}

int main ()
{
  Data data(1,2);
  std::cout << data << std::endl;

  // This will fail as std::bind will copy or move the arguments. arguments are
  // never passed by reference unless wrapped in std::ref or std::cref
  // https://en.cppreference.com/w/cpp/utility/functional/bind
  auto fail_func = std::bind (foo_cref, data);

  auto cref_func = std::bind (foo_cref, std::cref(data));
  std::cout << cref_func() << std::endl;
  std::cout << data << std::endl;

  // value could be updated inside the function object
  auto func_ref = std::bind (foo_ref, std::ref(data));
  std::cout << func_ref() << std::endl;
  std::cout << data << std::endl;

  return 0;
}

```

# Rerefence:
http://www.gockelhut.com/cpp-pirate/lambda-vs-bind.html

https://shawnliu.me/post/passing-reference-with-std-ref-in-c++/

https://github.com/peter-can-write/cpp-notes/blob/master/prefer-lambdas-over-std::bind.md
