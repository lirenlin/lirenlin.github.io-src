Title: python list slicing
Date: Sun  4 Aug 15:21:47 CEST 2019
Category: python
Tags: python

一个很好的总结:
[stackoverflow: Understanding slice notation](https://stackoverflow.com/questions/509211/understanding-slice-notation)

```
a[start:end:step] # items from start through  stop - 1. a[stop] not included.
```
当step为负数的时候，算法跟之前一样，[start, start+step, start+step+step, ..., end)

