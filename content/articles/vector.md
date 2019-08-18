Title: c++ std::vector
Date: Thu 20 Jun 20:50:00 CEST 2019
Category: C++
Tags: C++

# c++ range base for loop over vector
If you don't want to change the items as well as want to avoid making copies, then auto const & is the correct choice:
```
for (auto const &x : vec)
```

Whoever suggests you to use auto & is wrong. Ignore them.  
Here is recap:

* Choose `auto x` when you want to work with copies.
* Choose `auto &x` when you want to work with original items and may modify them.
* Choose `auto const &x` when you want to work with original items and will not modify them.



# Does “X& const x” make any sense?
referece is alwas const. You cannot modify it to reference another item.
reference to a const item is normally what people expect.
This is `const T& x`, instead of `T& const x`

# vector remove/erase idiom
```
std::vector<int>& vec = myNumbers; // use shorter name
vec.erase(std::remove(vec.begin(), vec.end(), number_in), vec.end());
```
1. Remove will not change the size of vector, it will shift other item forward to
overwrite the given item. An iterator to the next item will be returned.
2. erase is needed to erase those items starting from the iterator. The size of
the vector will also be updated accordingly.

# vector remove duplicate idiom
```
std::sort(vec.begin(), vec.end());
vec.erase(std::unique(vec.begin(), vec.end()), vec.end());
```
1. sort will make the items with same value consecutive in memory.
2. unique will shift items forward to eliminate all but the first element from
every consecutive group of equivalent elements from the range. It returns a
past-the-end iterator for the new logical end of the range.
3. erase will erase items in the range.



# Reference:
[c++ range based loop](https://stackoverflow.com/questions/15176104/c11-range-based-loop-get-item-by-value-or-reference-to-const)
[ISOCPP FAQ. Does “X& const x” make any sense?](https://isocpp.org/wiki/faq/const-correctness#const-ref-nonsense)
[stackoverflow: What's the most efficient way to erase duplicates and sort a vector?](https://stackoverflow.com/questions/1041620/whats-the-most-efficient-way-to-erase-duplicates-and-sort-a-vector)

