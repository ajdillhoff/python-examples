# `NumPy` Quickstart

This notebook is a quick introduction to `NumPy`. It is an interactive version of the [NumPy Quickstart Tutorial](https://docs.scipy.org/doc/numpy/user/quickstart.html).

All credits go to the original authors of the tutorial © Copyright 2008-2023, NumPy Developers.

# The Basics

NumPy’s main object is the homogeneous multidimensional array. It is a table of elements (usually numbers), all of the same type, indexed by a tuple of non-negative integers. In NumPy dimensions are called axes.

For example, the array for the coordinates of a point in 3D space, `[1, 2, 1]`, has one axis. That axis has 3 elements in it, so we say it has a length of 3. In the example pictured below, the array has 2 axes. The first axis has a length of 2, the second axis has a length of 3.

```
[[ 1., 0., 0.],
 [ 0., 1., 2.]]
```

NumPy’s array class is called `ndarray`. It is also known by the alias `array`. Note that `numpy.array` is not the same as the Standard Python Library class `array.array`, which only handles one-dimensional arrays and offers less functionality. The more important attributes of an `ndarray` object are:

**ndarray.ndim**

the number of axes (dimensions) of the array.

**ndarray.shape**

the dimensions of the array. This is a tuple of integers indicating the size of the array in each dimension. For a matrix with n rows and m columns, `shape` will be `(n,m)`. The length of the `shape` tuple is therefore the number of axes, `ndim`.

**ndarray.size**

the total number of elements of the array. This is equal to the product of the elements of `shape`.

**ndarray.dtype**

an object describing the type of the elements in the array. One can create or specify dtype’s using standard Python types. Additionally NumPy provides types of its own. numpy.int32, numpy.int16, and numpy.float64 are some examples.

**ndarray.itemsize**

the size in bytes of each element of the array. For example, an array of elements of type `float64` has `itemsize 8` (=64/8), while one of type `complex32` has `itemsize` 4 (=32/8). It is equivalent to `ndarray.dtype.itemsize`.

**ndarray.data**

the buffer containing the actual elements of the array. Normally, we won’t need to use this attribute because we will access the elements in an array using indexing facilities.


## An example


```python
import numpy as np

a = np.arange(15).reshape(3, 5)

print("a = \n{}".format(a))

print("a.shape = {}".format(a.shape))
print("a.ndim = {}".format(a.ndim))
print("a.dtype.name = {}".format(a.dtype.name))
print("a.itemsize = {}".format(a.itemsize))
print("a.size = {}".format(a.size))
print("type(a) = {}".format(type(a)))
```

    a = 
    [[ 0  1  2  3  4]
     [ 5  6  7  8  9]
     [10 11 12 13 14]]
    a.shape = (3, 5)
    a.ndim = 2
    a.dtype.name = int64
    a.itemsize = 8
    a.size = 15
    type(a) = <class 'numpy.ndarray'>


## Array Creation

There are several ways to create arrays.

For example, you can create an array from a regular Python list or tuple using the `array` function. The type of the resulting array is deduced from the type of the elements in the sequences.


```python
a = np.array([2,3,4])
print("a = {}".format(a))
print("a.dtype = {}".format(a.dtype))

b = np.array([1.2, 3.5, 5.1])
print("b = {}".format(b))
print("b.dtype = {}".format(b.dtype))
```

    a = [2 3 4]
    a.dtype = int64
    b = [1.2 3.5 5.1]
    b.dtype = float64


A frequent error consists in calling array with multiple numeric arguments, rather than providing a single list of numbers as an argument.


```python
a = np.array(1, 2, 3, 4) # WRONG
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    /home/alex/dev/teaching/python-examples/numpy/quickstart.ipynb Cell 6 line 1
    ----> <a href='vscode-notebook-cell:/home/alex/dev/teaching/python-examples/numpy/quickstart.ipynb#X14sZmlsZQ%3D%3D?line=0'>1</a> a = np.array(1, 2, 3, 4)


    TypeError: array() takes from 1 to 2 positional arguments but 4 were given



```python
a = np.array([1, 2, 3, 4]) # RIGHT
```

`array` transforms sequences of sequences into two-dimensional arrays, sequences of sequences of sequences into three-dimensional arrays, and so on.


```python
b = np.array([(1.5, 2, 3), (4, 5, 6)])
print("b =\n{}".format(b))
```

    b = [[1.5 2.  3. ]
     [4.  5.  6. ]]


The type of the array can also be explicitly specified at creation time:


```python
c = np.array([[1, 2], [3, 4]], dtype=complex)
print("c =\n{}".format(c))
```

    c =
    [[1.+0.j 2.+0.j]
     [3.+0.j 4.+0.j]]


Often, the elements of an array are originally unknown, but its size is known. Hence, NumPy offers several functions to create arrays with initial placeholder content. These minimize the necessity of growing arrays, an expensive operation.

The function `zeros` creates an array full of zeros, the function `ones` creates an array full of ones, and the function `empty` creates an array whose initial content is random and depends on the state of the memory. By default, the dtype of the created array is `float64`.


```python
print("np.zeros((3, 4)) =\n{}".format(np.zeros((3, 4))))
print("np.ones((2, 3, 4), dtype=np.int16) =\n{}".format(np.ones((2, 3, 4), dtype=np.int16)))
print("np.empty((2, 3)) =\n{}".format(np.empty((2, 3))))
```

    np.zeros((3, 4)) =
    [[0. 0. 0. 0.]
     [0. 0. 0. 0.]
     [0. 0. 0. 0.]]
    np.ones((2, 3, 4), dtype=np.int16) =
    [[[1 1 1 1]
      [1 1 1 1]
      [1 1 1 1]]
    
     [[1 1 1 1]
      [1 1 1 1]
      [1 1 1 1]]]
    np.empty((2, 3)) =
    [[1.39069238e-309 1.39069238e-309 1.39069238e-309]
     [1.39069238e-309 1.39069238e-309 1.39069238e-309]]


To create sequences of numbers, NumPy provides the `arange` function which is analogous to the Python built-in `range`, but returns an array.


```python
print("np.arange(10, 30, 5) = {}".format(np.arange(10, 30, 5)))
print("np.arange(0, 2, 0.3) = {}".format(np.arange(0, 2, 0.3))) # it accepts float arguments
```

    np.arange(10, 30, 5) = [10 15 20 25]
    np.arange(0, 2, 0.3) = [0.  0.3 0.6 0.9 1.2 1.5 1.8]


When `arange` is used with floating point arguments, it is generally not possible to predict the number of elements obtained, due to the finite floating point precision. For this reason, it is usually better to use the function `linspace` that receives as an argument the number of elements that we want, instead of the step:


```python
from numpy import pi

print("np.linspace(0, 2, 9) = {}".format(np.linspace(0, 2, 9))) # 9 numbers from 0 to 2
x = np.linspace(0, 2*pi, 100) # useful to evaluate function at lots of points
f = np.sin(x)
```

    np.linspace(0, 2, 9) = [0.   0.25 0.5  0.75 1.   1.25 1.5  1.75 2.  ]


## Print Arrays

When you print an array, NumPy displays it in a similar way to nested lists, but with the following layout:
-  the last axis is printed from left to right,
-  the second-to-last is printed from top to bottom,
-  the rest are also printed from top to bottom, with each slice separated from the next by an empty line.

One-dimensional arrays are then printed as rows, bidimensionals as matrices and tridimensionals as lists of matrices.


```python
a = np.arange(6) # 1d array
print("a =\n{}".format(a))

b = np.arange(12).reshape(4, 3) # 2d array
print("b =\n{}".format(b))

c = np.arange(24).reshape(2, 3, 4) # 3d array
print("c =\n{}".format(c))
```

    a =
    [0 1 2 3 4 5]
    b =
    [[ 0  1  2]
     [ 3  4  5]
     [ 6  7  8]
     [ 9 10 11]]
    c =
    [[[ 0  1  2  3]
      [ 4  5  6  7]
      [ 8  9 10 11]]
    
     [[12 13 14 15]
      [16 17 18 19]
      [20 21 22 23]]]


If an array is too large to be printed, NumPy automatically skips the central part of the array and only prints the corners:


```python
print("np.arange(10000) = {}".format(np.arange(10000)))
print("np.arange(10000).reshape(100, 100) =\n{}".format(np.arange(10000).reshape(100, 100)))
```

    np.arange(10000) = [   0    1    2 ... 9997 9998 9999]
    np.arange(10000).reshape(100, 100) =
    [[   0    1    2 ...   97   98   99]
     [ 100  101  102 ...  197  198  199]
     [ 200  201  202 ...  297  298  299]
     ...
     [9700 9701 9702 ... 9797 9798 9799]
     [9800 9801 9802 ... 9897 9898 9899]
     [9900 9901 9902 ... 9997 9998 9999]]


To disable this behaviour and force NumPy to print the entire array, you can change the printing options using `set_printoptions`.


```python
import sys
np.set_printoptions(threshold=sys.maxsize) # force NumPy to print the entire array
```

## Basic Operations

Arithmetic operators on arrays apply elementwise. A new array is created and filled with the result.


```python
a = np.array([20, 30, 40, 50])
b = np.arange(4)
print("b =\n{}".format(b))

c = a - b
print("c =\n{}".format(c))

print("b**2 =\n{}".format(b**2))

print("10*np.sin(a) =\n{}".format(10*np.sin(a)))

print("a < 35 =\n{}".format(a < 35))
```

    b =
    [0 1 2 3]
    c =
    [20 29 38 47]
    b**2 =
    [0 1 4 9]
    10*np.sin(a) =
    [ 9.12945251 -9.88031624  7.4511316  -2.62374854]
    a < 35 =
    [ True  True False False]


Unlike in many matrix languages, the product operator `*` operates elementwise in NumPy arrays. The matrix product can be performed using the `@` operator (in python >=3.5) or the dot function or method:


```python
A = np.array([[1, 1], [0, 1]])
B = np.array([[2, 0], [3, 4]])

print("A *  B =\n{}".format(A * B)) # elementwise product

print("A @ B =\n{}".format(A @ B)) # matrix product

print("A.dot(B) =\n{}".format(A.dot(B))) # another matrix product
```

    A *  B =
    [[2 0]
     [0 4]]
    A @ B =
    [[5 4]
     [3 4]]
    A.dot(B) =
    [[5 4]
     [3 4]]


Some operations, such as `+=` and `*=`, act in place to modify an existing array rather than create a new one.


```python
rg = np.random.default_rng(1) # create instance of default random number generator
a = np.ones((2, 3), dtype=int)
b = rg.random((2, 3))
a *= 3

print("a =\n{}".format(a))

b += a

print("b =\n{}".format(b))

a += b # b is not automatically converted to integer type
```

    a =
    [[3 3 3]
     [3 3 3]]
    b =
    [[3.51182162 3.9504637  3.14415961]
     [3.94864945 3.31183145 3.42332645]]



    ---------------------------------------------------------------------------

    UFuncTypeError                            Traceback (most recent call last)

    /home/alex/dev/teaching/python-examples/numpy/quickstart.ipynb Cell 29 line 1
          <a href='vscode-notebook-cell:/home/alex/dev/teaching/python-examples/numpy/quickstart.ipynb#Y110sZmlsZQ%3D%3D?line=7'>8</a> b += a
         <a href='vscode-notebook-cell:/home/alex/dev/teaching/python-examples/numpy/quickstart.ipynb#Y110sZmlsZQ%3D%3D?line=9'>10</a> print("b =\n{}".format(b))
    ---> <a href='vscode-notebook-cell:/home/alex/dev/teaching/python-examples/numpy/quickstart.ipynb#Y110sZmlsZQ%3D%3D?line=11'>12</a> a += b


    UFuncTypeError: Cannot cast ufunc 'add' output from dtype('float64') to dtype('int64') with casting rule 'same_kind'


When operating with arrays of different types, the type of the resulting array corresponds to the more general or precise one (a behavior known as upcasting).


```python
a = np.ones(3, dtype=np.int32)
b = np.linspace(0, pi, 3)

print("b.dtype.name = {}".format(b.dtype.name))

c = a + b

print("c =\n{}".format(c))
print("c.dtype.name = {}".format(c.dtype.name))

d = np.exp(c*1j)

print("d =\n{}".format(d))
print("d.dtype.name = {}".format(d.dtype.name))
```

    b.dtype.name = float64
    c =
    [1.         2.57079633 4.14159265]
    c.dtype.name = float64
    d =
    [ 0.54030231+0.84147098j -0.84147098+0.54030231j -0.54030231-0.84147098j]
    d.dtype.name = complex128


Many unary operations, such as computing the sum of all the elements in the array, are implemented as methods of the `ndarray` class.


```python
a = rg.random((2, 3))
print("a =\n{}".format(a))

print("a.sum() = {}".format(a.sum()))
print("a.min() = {}".format(a.min()))
print("a.max() = {}".format(a.max()))
```

    a =
    [[0.82770259 0.40919914 0.54959369]
     [0.02755911 0.75351311 0.53814331]]
    a.sum() = 3.1057109529998157
    a.min() = 0.027559113243068367
    a.max() = 0.8277025938204418


By default, these operations apply to the array as though it were a list of numbers, regardless of its shape. However, by specifying the `axis` parameter you can apply an operation along the specified axis of an array:


```python
b = np.arange(12).reshape(3, 4)
print("b =\n{}".format(b))

print("b.sum(axis=0) = {}".format(b.sum(axis=0))) # sum of each column
print("b.min(axis=1) = {}".format(b.min(axis=1))) # min of each row
print("b.cumsum(axis=1) =\n{}".format(b.cumsum(axis=1))) # cumulative sum along each row
```

    b =
    [[ 0  1  2  3]
     [ 4  5  6  7]
     [ 8  9 10 11]]
    b.sum(axis=0) = [12 15 18 21]
    b.min(axis=1) = [0 4 8]
    b.cumsum(axis=1) =
    [[ 0  1  3  6]
     [ 4  9 15 22]
     [ 8 17 27 38]]


## Universal Functions

NumPy provides familiar mathematical functions such as sin, cos, and exp. In NumPy, these are called “universal functions”(`ufunc`). Within NumPy, these functions operate elementwise on an array, producing an array as output.


```python
B = np.arange(3)
print("B = {}".format(B))

print("np.exp(B) = {}".format(np.exp(B)))
print("np.sqrt(B) = {}".format(np.sqrt(B)))

C = np.array([2., -1., 4.])

print("np.add(B, C) = {}".format(np.add(B, C)))
```

    B = [0 1 2]
    np.exp(B) = [1.         2.71828183 7.3890561 ]
    np.sqrt(B) = [0.         1.         1.41421356]
    np.add(B, C) = [2. 0. 6.]


## Indexing, Slicing and Iterating

One-dimensional arrays can be indexed, sliced and iterated over, much like lists and other Python sequences.


```python
a = np.arange(10)**3

print("a = {}".format(a))
print("a[2] = {}".format(a[2]))
print("a[2:5] = {}".format(a[2:5]))

a[:6:2] = -1000 # equivalent to a[0:6:2] = -1000
                # from start to position 6, exclusive, set every 2nd element to -1000

print("a = {}".format(a))
print("a[ : :-1] = {}".format(a[ : :-1])) # reversed a

for i in a:
    print(i**(1/3.))
```

    a = [  0   1   8  27  64 125 216 343 512 729]
    a[2] = 8
    a[2:5] = [ 8 27 64]
    a = [-1000     1 -1000    27 -1000   125   216   343   512   729]
    a[ : :-1] = [  729   512   343   216   125 -1000    27 -1000     1 -1000]
    nan
    1.0
    nan
    3.0
    nan
    4.999999999999999
    5.999999999999999
    6.999999999999999
    7.999999999999999
    8.999999999999998


    /tmp/ipykernel_15700/4153428083.py:14: RuntimeWarning: invalid value encountered in power
      print(i**(1/3.))


Multidimensional arrays can have one index per axis. These indices are given in a tuple separated by commas:


```python
def f(x, y):
    return 10 * x + y

b = np.fromfunction(f, (5, 4), dtype=int)
print("b =\n{}".format(b))

print("b[2, 3] = {}".format(b[2, 3]))
print("b[0:5, 1] = {}".format(b[0:5, 1])) # each row in the second column of b
print("b[ : , 1] = {}".format(b[ : , 1])) # equivalent to the previous example
print("b[1:3, : ] =\n{}".format(b[1:3, : ])) # each column in the second and third row of b
```

    b =
    [[ 0  1  2  3]
     [10 11 12 13]
     [20 21 22 23]
     [30 31 32 33]
     [40 41 42 43]]
    b[2, 3] = 23
    b[0:5, 1] = [ 1 11 21 31 41]
    b[ : , 1] = [ 1 11 21 31 41]
    b[1:3, : ] =
    [[10 11 12 13]
     [20 21 22 23]]


When fewer indices are provided than the number of axes, the missing indices are considered complete slices:


```python
print("b[-1] = {}".format(b[-1])) # the last row. Equivalent to b[-1, : ]
```

    b[-1] = [40 41 42 43]


The expression within brackets in `b[i]` is treated as an `i` followed by as many instances of `:` as needed to represent the remaining axes. NumPy also allows you to write this using dots as `b[i,...]`.

The `dots` (`...`) represent as many colons as needed to produce a complete indexing tuple. For example, if `x` is an array with 5 axes, then
- `x[1,2,...]` is equivalent to `x[1,2,:,:,:]`,
- `x[...,3]` to `x[:,:,:,:,3]` and
- `x[4,...,5,:]` to `x[4,:,:,5,:]`.


```python
c = np.array([[[  0,  1,  2], # a 3D array (two stacked 2D arrays)
                [ 10, 12, 13]],
                [[100,101,102],
                [110,112,113]]])

print("c.shape = {}".format(c.shape))
print("c[1,...] =\n{}".format(c[1,...])) # same as c[1,:,:] or c[1]
print("c[...,2] =\n{}".format(c[...,2])) # same as c[:,:,2]
```

    c.shape = (2, 2, 3)
    c[1,...] =
    [[100 101 102]
     [110 112 113]]
    c[...,2] =
    [[  2  13]
     [102 113]]


Iterating over multidimensional arrays is done with respect to the first axis:


```python
for row in b:
    print(row)
```

    [0 1 2 3]
    [10 11 12 13]
    [20 21 22 23]
    [30 31 32 33]
    [40 41 42 43]

