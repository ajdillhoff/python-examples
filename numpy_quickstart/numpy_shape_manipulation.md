# `NumPy` Quickstart

This notebook is a quick introduction to `NumPy`. It is an interactive version of the [NumPy Quickstart Tutorial](https://docs.scipy.org/doc/numpy/user/quickstart.html).

All credits go to the original authors of the tutorial © Copyright 2008-2023, NumPy Developers.

# Shape Manipulation

## Changing the shape of an array

An array has a shape given by the number of elements along each axis:


```python
import numpy as np

a = np.floor(10 * np.random.random((3,4)))

print("a = \n{}".format(a))
print("a.shape = {}".format(a.shape))
```

    a = 
    [[6. 7. 2. 1.]
     [5. 9. 4. 9.]
     [3. 5. 3. 2.]]
    a.shape = (3, 4)


The shape of an array can be changed with various commands. Note that the following three commands all return a modified array, but do not change the original array:


```python
print("a.ravel() = {}".format(a.ravel())) # flatten the array
print("a.reshape(6,2) = \n{}".format(a.reshape(6,2))) # reshape the array
print("a.T = \n{}".format(a.T)) # transpose the array
print("a.T.shape = {}".format(a.T.shape))
```

    a.ravel() = [6. 7. 2. 1. 5. 9. 4. 9. 3. 5. 3. 2.]
    a.reshape(6,2) = 
    [[6. 7.]
     [2. 1.]
     [5. 9.]
     [4. 9.]
     [3. 5.]
     [3. 2.]]
    a.T = 
    [[6. 5. 3.]
     [7. 9. 5.]
     [2. 4. 3.]
     [1. 9. 2.]]
    a.T.shape = (4, 3)


The order of the elements in the array resulting from `ravel` is normally “C-style”, that is, the rightmost index “changes the fastest”, so the element after `a[0,0]` is `a[0,1]`. If the array is reshaped to some other shape, again the array is treated as “C-style”. NumPy normally creates arrays stored in this order, so `ravel` will usually not need to copy its argument, but if the array was made by taking slices of another array or created with unusual options, it may need to be copied. The functions `ravel` and `reshape` can also be instructed, using an optional argument, to use FORTRAN-style arrays, in which the leftmost index changes the fastest.

The `reshape` function returns its argument with a modified shape, whereas the `ndarray.resize` method modifies the array itself:


```python
a.resize((2,6)) # resize the array
print("a.resize((2,6)) = \n{}".format(a))
```

    a.resize((2,6)) = 
    [[6. 7. 2. 1. 5. 9.]
     [4. 9. 3. 5. 3. 2.]]


If a dimension is given as -1 in a reshaping operation, the other dimensions are automatically calculated:


```python
print("a.reshape(3, -1) = \n{}".format(a.reshape(3, -1)))
```

    a.reshape(3, -1) = 
    [[6. 7. 2. 1.]
     [5. 9. 4. 9.]
     [3. 5. 3. 2.]]


## Stacking together different arrays

Several arrays can be stacked together along different axes:


```python
a = np.floor(10 * np.random.random((2,2)))
print("a = \n{}".format(a))

b = np.floor(10 * np.random.random((2,2)))
print("b = \n{}".format(b))

print("np.vstack((a,b)) = \n{}".format(np.vstack((a,b))))

print("np.hstack((a,b)) = \n{}".format(np.hstack((a,b))))
```

    a = 
    [[8. 0.]
     [5. 1.]]
    b = 
    [[7. 7.]
     [0. 1.]]
    np.vstack((a,b)) = 
    [[8. 0.]
     [5. 1.]
     [7. 7.]
     [0. 1.]]
    np.hstack((a,b)) = 
    [[8. 0. 7. 7.]
     [5. 1. 0. 1.]]


The function `column_stack` stacks 1D arrays as columns into a 2D array. It is equivalent to `hstack` only for 2D arrays:


```python
from numpy import newaxis

print("np.column_stack((a,b)) = \n{}".format(np.column_stack((a,b)))) # with 2D arrays

a = np.array([4.,2.])
b = np.array([3.,8.])

print("np.column_stack((a,b)) = \n{}".format(np.column_stack((a,b)))) # returns a 2D array
print("np.hstack((a,b)) = \n{}".format(np.hstack((a,b)))) # returns a 1D array
print("a[:,newaxis] = \n{}".format(a[:,newaxis])) # view a as a 2D column vector
print("np.column_stack((a[:,newaxis],b[:,newaxis])) = \n{}".format(np.column_stack((a[:,newaxis],b[:,newaxis]))))
print("np.hstack((a[:,newaxis],b[:,newaxis])) = \n{}".format(np.hstack((a[:,newaxis],b[:,newaxis]))))
```

    np.column_stack((a,b)) = 
    [[4. 3.]
     [2. 8.]]
    np.column_stack((a,b)) = 
    [[4. 3.]
     [2. 8.]]
    np.hstack((a,b)) = 
    [4. 2. 3. 8.]
    a[:,newaxis] = 
    [[4.]
     [2.]]
    np.column_stack((a[:,newaxis],b[:,newaxis])) = 
    [[4. 3.]
     [2. 8.]]
    np.hstack((a[:,newaxis],b[:,newaxis])) = 
    [[4. 3.]
     [2. 8.]]


In general, for arrays of with more than two dimensions, `hstack` stacks along their second axes, `vstack` stacks along their first axes, and `concatenate` allows for an optional arguments giving the number of the axis along which the concatenation should happen.

**Note**

In complex cases, `r_` and `c_` are useful for creating arrays by stacking numbers along one axis. They allow the use of range literals `:`


```python
print("np.r_[1:4,0,4] = \n{}".format(np.r_[1:4,0,4])) # concatenate along the first axis
```

    np.r_[1:4,0,4] = 
    [1 2 3 0 4]


When used with arrays as arguments, `r_` and `c_` are similar to `vstack` and `hstack` in their default behavior, but allow for an optional argument giving the number of the axis along which to concatenate.

## Splitting one array into several smaller ones

Using `hsplit`, you can split an array along its horizontal axis, either by specifying the number of equally shaped arrays to return, or by specifying the columns after which the division should occur:


```python
a = np.floor(10 * np.random.random((2,12)))
print("a = \n{}".format(a))

# split a into 3
print("np.hsplit(a,3) = \n{}".format(np.hsplit(a,3)))

# split a after the third and the fourth column
print("np.hsplit(a,(3,4)) = \n{}".format(np.hsplit(a,(3,4))))
```

    a = 
    [[7. 0. 8. 1. 4. 7. 8. 1. 1. 8. 1. 2.]
     [6. 7. 7. 5. 7. 5. 0. 7. 7. 4. 6. 1.]]
    np.hsplit(a,3) = 
    [array([[7., 0., 8., 1.],
           [6., 7., 7., 5.]]), array([[4., 7., 8., 1.],
           [7., 5., 0., 7.]]), array([[1., 8., 1., 2.],
           [7., 4., 6., 1.]])]
    np.hsplit(a,(3,4)) = 
    [array([[7., 0., 8.],
           [6., 7., 7.]]), array([[1.],
           [5.]]), array([[4., 7., 8., 1., 1., 8., 1., 2.],
           [7., 5., 0., 7., 7., 4., 6., 1.]])]


`vsplit` splits along the vertical axis, and `array_split` allows one to specify along which axis to split.
