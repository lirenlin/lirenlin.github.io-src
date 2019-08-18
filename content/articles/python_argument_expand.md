Title: Python argument expansion
Date: Sat 17 Aug 12:10:31 CEST 2019
Category: Python
Tags: Python

* \* operator: positional argument expansion
for a list, expand to function call argument list

* \*\* operator: keyword argument expansion for a dictionary, expand to function call keyword argument list

```
def add(a, b):
  print a+b

a = [1, 2]
kwargs={'b':1, 'a': 1}
add(*a)
add(**kwargs)


def add(a, *args, **kwargs):
  print a      # positional argument
  print args   # a list
  print kwargs # a dict
```

