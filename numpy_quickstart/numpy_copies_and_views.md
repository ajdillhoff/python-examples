# `NumPy` Quickstart

This notebook is a quick introduction to `NumPy`. It is an interactive version of the [NumPy Quickstart Tutorial](https://docs.scipy.org/doc/numpy/user/quickstart.html).

All credits go to the original authors of the tutorial © Copyright 2008-2023, NumPy Developers.

# Copies and Views

When operating and manipulating arrays, their data is sometimes copied into a new array and sometimes not. This is often a source of confusion for beginners. There are three cases:

## No Copy at All

Simple assignments make no copy of array objects or of their data.


```python
import numpy as np

a = np.array([[0, 1, 2, 3],
              [4, 5, 6, 7],
              [8, 9, 10, 11]])

b = a # no new object is created
print(b is a) # a and b are two names for the same ndarray object
```

    True


Python passes mutable objects as references, so function calls make no copy.


```python
def f(x):
    print(id(x))

print(id(a)) # id is a unique identifier of an object

f(a) # a is passed to the function under the name x
```

    139846954913200
    139846954913200


## View or Shallow Copy

Different array objects can share the same data. The `view` method creates a new array object that looks at the same data.


```python
c = a.view() # c is a view of the data owned by a

print("c is a = {}".format(c is a))
print("c.base is a = {}".format(c.base is a)) # c is a view of the data owned by a
print("c.flags.owndata = {}".format(c.flags.owndata)) # c does not own the data

c = c.reshape((2, 6)) # a's shape doesn't change
print("a.shape = {}".format(a.shape))

c[0, 4] = 1234 # a's data changes
print("a =\n{}".format(a))
```

    c is a = False
    c.base is a = True
    c.flags.owndata = False
    a.shape = (3, 4)
    a =
    [[   0    1    2    3]
     [1234    5    6    7]
     [   8    9   10   11]]


Slicing an array returns a view of it:


```python
s = a[:, 1:3]
s[:] = 10 # s[:] is a view of s. Note the difference between s=10 and s[:]=10

print("a =\n{}".format(a))
```

    a =
    [[   0   10   10    3]
     [1234   10   10    7]
     [   8   10   10   11]]


## Deep Copy

The `copy` method makes a complete copy of the array and its data.


```python
d = a.copy() # a new array object with new data is created

print("d is a = {}".format(d is a))
print("d.base is a = {}".format(d.base is a)) # d doesn't share anything with a

d[0, 0] = 9999

print("a =\n{}".format(a))
```

    d is a = False
    d.base is a = False
    a =
    [[   0   10   10    3]
     [1234   10   10    7]
     [   8   10   10   11]]


Sometimes `copy` should be called after slicing if the original array is not required anymore. For example, suppose a is a huge intermediate result and the final result b only contains a small fraction of a, a deep copy should be made when constructing b with slicing:


```python
a = np.arange(int(1e8))
b = a[:100].copy()

del a # the memory of ``a`` can be released.
```

If `b = a[:100]` is used instead, `a` is referenced by `b` and will persist in memory even if `del a` is executed.

## Functions and Methods Overview

See [Routines](https://docs.scipy.org/doc/numpy/reference/routines.html#routines) for the full list of routines available in NumPy.
