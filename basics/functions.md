# Functions

We learned the importance of functions early on in mathematics. It is a compact way of represented a complex process dependent on a set of variables. In programming, functions are used to encapsulate a set of instructions that are used repeatedly. Functions are also used to make code more readable and easier to debug.

In this notebook, we will look at a few important built-in functions in Python as well as how to define our own functions.

## Built-in Functions

Python has a good number of built-in functions that cover a general range of tasks. 


```python
# Find the max of a list of numbers
max_val = max(1, 2, 3)
print(f"The max value is {max_val}")

# Find the min of a list of numbers
min_val = min(1, 2, 3)
print(f"The min value is {min_val}")

# Get the length of a string
text = input("Enter some text: ")
print(f"The length of \"{text}\" is {len(text)}")
```

    The max value is 3
    The min value is 1
    The length of "test" is 4


The `len` function returns the length of a string, list, or other iterable object. Since these functions are built-in, we should treat them as keywords. However, we can still overwrite them if we want to.

## Type Conversion Functions

Python has built-in functions to convert between data types. These are `int`, `float`, `str`, `bool`, and `list`. Converting between incompatible types will result in an error.


```python
# Try entering a number and text
val = input("Enter a number: ")
val_int = int(val)
print(f"The value of {val} is {val_int}")

# Converting an integer type to float will truncate the decimal value
float_val = 3.14
int_val = int(float_val)
print(f"The value of {float_val} is {int_val}")

# Converting a number to a string also has its uses
big_number = 184759372934
big_number_str = str(big_number)
print(f"There are {len(big_number_str)} digits in {big_number_str}")
```

    The value of 10 is 10
    The value of 3.14 is 3
    There are 12 digits in 184759372934


## Math Functions

Python has many more functions that are available through named modules. For example, the `math` module contains many useful functions for mathematical operations. To use these functions, we need to import the module first.


```python
import math

signal_power = 10
noise_power = 5
ratio = signal_power / noise_power
decibels = 10 * math.log10(ratio)
print(f"The decibel value is {decibels}")

# The math module also has a function to convert from radians to degrees
radians = 0.7
degrees = math.degrees(radians)
print(f"{radians} radians is {degrees} degrees")

# The math module also has a function to convert from degrees to radians
degrees = 45
radians = math.radians(degrees)
print(f"{degrees} degrees is {radians} radians")
```

    The decibel value is 3.010299956639812
    0.7 radians is 40.10704565915762 degrees
    45 degrees is 0.7853981633974483 radians


### Example: Getting the number of digits without `len`

We can use the `math.log10` function to get the number of digits in a number.


```python
big_number = 184759372934
big_number_log = math.log10(big_number)
print(f"The log of {big_number} is {big_number_log}")

# We can use this to get the number of digits in a number
big_number_log_int = int(big_number_log)
print(f"There are {big_number_log_int + 1} digits in {big_number}")


```

    The log of 184759372934 is 11.266606479598726
    There are 12 digits in 184759372934


## Random Numbers

The `random` module contains functions for generating random numbers. The `random` function returns a random number between 0 and 1. The `randint` function returns a random integer between two numbers. Other functions in the `random` module include `randrange`, `choice`, `choices`, `shuffle`, and `sample`.


```python
import random

# Generate 10 random numbers between 0 and 1
for i in range(10):
    print(random.random())

# Generate 10 random integers between 4 and 10
for i in range(10):
    print(random.randint(4, 10))

# Randomly select a value from a list
outcomes = ["rock", "paper", "scissors"]
print(random.choice(outcomes))
```

    0.5791115192498043
    0.25376108559783617
    0.3024994224981705
    0.09072083021401978
    0.42037740159252324
    0.6617409553852582
    0.4379309412534801
    0.2475132325137145
    0.8452657960508129
    0.9268148237541722
    4
    5
    7
    5
    7
    10
    8
    6
    7
    4
    scissors


Third-party modules such as `numpy` and `scipy` contain many more functions for generating random numbers.


```python
import numpy as np

# Generate 10 random numbers between 0 and 1
numbers = np.random.rand(10)
print(numbers)

# Sample 10 random numbers from a normal distribution
numbers = np.random.randn(10)
print(numbers)
```

    [0.47426298 0.22698408 0.42633457 0.97584666 0.68835279 0.57067918
     0.56958053 0.86689698 0.54039587 0.59397872]
    [ 0.97783258 -0.4043045   0.05416324 -2.21162364 -0.60327265 -0.39077797
     -0.83294774  0.56285811 -0.28047169 -0.60044315]


## Defining Functions

We can define our own functions using the `def` keyword. The syntax for defining a function is as follows:

```python
def function_name(parameters):
    # function body
    return value
```

Python functions can have multiple parameters and return multiple values. The `return` keyword is optional. If it is not used, the function will return `None`.


```python
import math

def calculate_stats(numbers):
    """Calculate the mean and standard deviation of a list of numbers"""
    mean = sum(numbers) / len(numbers)
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    std_dev = math.sqrt(variance)
    return mean, std_dev

# Calculate the mean and standard deviation of a list of numbers
numbers = [1, 2, 3, 4, 5]
mean, std_dev = calculate_stats(numbers)
print(f"The mean is {mean} and the standard deviation is {std_dev}")
```

    The mean is 3.0 and the standard deviation is 1.4142135623730951


# Default Argument Values

Python functions can have default values for their arguments. This allows us to call the function without specifying the value for that argument. If we do not specify a value for an argument, the default value will be used.


```python
# To demonstrate default argument values, let's make a function that
# allows the user to select the axis along which to calculate the mean
def calculate_mean(numbers, axis=0):
    """Calculates the mean of a 2D array along a given axis"""
    # Check that the input is a 2D python list
    if not isinstance(numbers, list) or not isinstance(numbers[0], list):
        raise ValueError("Input must be a 2D list")

    if axis == 0:
        # Here, zip(*numbers) will return a list of tuples,
        # where each tuple is a column of our 2D list.
        return [sum(col) / len(col) for col in zip(*numbers)]
    elif axis == 1:
        return [sum(row) / len(row) for row in numbers]
    else:
        raise ValueError("Invalid axis value")
    
# Calculate the mean along the rows
numbers = [[1, 2, 3], [4, 5, 6]]
mean = calculate_mean(numbers, axis=1)
print("Mean of each row:", mean)

# Calculate the mean along the columns
numbers = [[1, 2, 3], [4, 5, 6]]
mean = calculate_mean(numbers, axis=0)
print("Mean of each column", mean)
```

    Mean of each row: [2.0, 5.0]
    Mean of each column [2.5, 3.5, 4.5]


# Keyword Arguments

Python functions can also have keyword arguments. This allows us to specify the name of the argument when calling the function. This is useful when a function has many arguments and we only want to specify a few of them.


```python
def matrix_max(matrix, axis=0, return_indices=False):
    """Calculates the maximum of a 2D array along a given axis"""
    # Check that the input is a 2D python list
    if not isinstance(matrix, list) or not isinstance(matrix[0], list):
        raise ValueError("Input must be a 2D list")

    if axis == 0:
        # Here, zip(*matrix) will return a list of tuples,
        # where each tuple is a column of our 2D list.
        max_vals = [max(col) for col in zip(*matrix)]
        if return_indices:
            max_indices = [col.index(max(col)) for col in zip(*matrix)]
            return max_vals, max_indices
        else:
            return max_vals
    elif axis == 1:
        max_vals = [max(row) for row in matrix]
        if return_indices:
            max_indices = [row.index(max(row)) for row in matrix]
            return max_vals, max_indices
        else:
            return max_vals
    else:
        raise ValueError("Invalid axis value")
    
# Calculate the max along the rows
numbers = [[1, 2, 3], [4, 5, 6]]
max_vals = matrix_max(numbers, axis=1)
print("Max of each row:", max_vals)

# Calculate the max along the columns
numbers = [[1, 2, 3], [4, 5, 6]]
max_vals = matrix_max(numbers, axis=0)
print("Max of each column", max_vals)

# Calculate the max along the rows and return the indices
numbers = [[1, 2, 3], [4, 5, 6]]
max_vals, max_indices = matrix_max(numbers, axis=1, return_indices=True)
print("Max of each row:", max_vals)
print("Indices of max values:", max_indices)
```

    Max of each row: [3, 6]
    Max of each column [4, 5, 6]
    Max of each row: [3, 6]
    Indices of max values: [2, 2]


# List Unpacking and Variable Arguments

Python functions can have variable arguments. This allows us to pass in a variable number of arguments to a function. The `*` operator is used to unpack a list or tuple into separate arguments.


```python
# The range function expects up to 3 arguments: start, stop, and step
# We can use list unpacking to put our arguments in a list
args = [1, 10, 2]
for i in range(*args):
    print(i)
```

    1
    3
    5
    7
    9



```python
# We can create a function that support multiple arguments as well as keyword arguments
def print_args(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

print_args(1, 2, 3, a=4, b=5)
```

    Positional arguments: (1, 2, 3)
    Keyword arguments: {'a': 4, 'b': 5}

