# Lists and List Comprehensions

List comprehensions provide a concise way to create lists, and are often faster than using a for-loop. They are inspired by set-builder notation in mathematics.

This notebook demonstrates common list functions as well as the syntax and basic usage of list comprehensions.


```python
names = ["Naomi", "James", "Amos", "Bobbie"]

# Append "Miller" to the end of the list
names.append("Miller")
# This can also be accomplished using the + operator or the extend() method

# These are similar, where `+=` is shorthand for `extend`
names.extend(["Chrisjen"])
names += ["Alex"]

# `extend()` works on any iterable
names.extend(["Fred", "Dawes", "Ashford"])

# This can also be done using slicing
# names[len(names):] = ["Fred", "Dawes", "Ashford"]

# Insert "Holden" at the beginning of the list
names.insert(0, "Holden")

# We can easily remove items
names.remove("Alex")

# We can also remove items by value
names.remove("Ashford")

# We can also remove items by index. This will return the removed item
eros_passenger = names.pop(5)
print(eros_passenger + " is on his way to Venus")

# If your list has duplicates, you can count the number of times a value appears
print("Naomi" + " appears " + str(names.count("Naomi")) + " time(s)")

# Reversing a list is easy
names.reverse()

# We can also create a shallow copy of a list
names_copy = names.copy()
```

    Miller is on his way to Venus
    Naomi appears 1 time(s)


## Sorting

A list can be sorted by calling the `sort` function. The list is sorted in-place, meaning that the original list is modified. Since a list can contain any type of object, the objects must be comparable to each other. For example, a list of strings can be sorted alphabetically, but a list of strings and integers cannot be sorted.

In cases with mixed types, a custom `key` function can be passed to the `sort` function. The `key` function is called on each element of the list, and the return value is used to sort the list. For example, to sort a list of strings and integers by the length of the string, the `key` function would transform the integers into strings.

```python
>>> l = ['abc', 1, 'ab']
>>> l.sort(key=str)
>>> l
[1, 'abc', 'ab']
```


```python
# Sorting is a very common operation, and Python gives us some level of control over how the items are sorted.
# The default is to sort in ascending order

# Sort the list in ascending order
names.sort()
print(names)

# Sort the list in descending order
names.sort(reverse=True)
print(names)

# We can also sort by a key function, such as the length of each name
names.sort(key=len)
print(names)

```

    ['Amos', 'Bobbie', 'Chrisjen', 'Dawes', 'Fred', 'Holden', 'James', 'Naomi']
    ['Naomi', 'James', 'Holden', 'Fred', 'Dawes', 'Chrisjen', 'Bobbie', 'Amos']
    ['Fred', 'Amos', 'Naomi', 'James', 'Dawes', 'Holden', 'Bobbie', 'Chrisjen']


Let's introduce a slightly more complex scenario in which each person in the list rolls a 20-sided die. We'll use the random module to generate a random number between 1 and 20 for each person. Using those values, we can then sort the list by the roll of the die, in descending order.


```python
import random

# Roll a 20-sided die for each person using a for loop
# rolls = []
# for name in names:
#     rolls.append(random.randint(1, 20))

# The above code is commented out by default because it can be written more succinctly using a list comprehension
rolls = [random.randint(1, 20) for _ in names]

print(names)
names.index('Fred')

# Sort the names by the roll of the die, in descending order
# First, create a function that returns the roll based on the name
def get_roll(name):
    # print(names) # reveals an empty list!
    return rolls[names.index(name)]

# names.sort(key=get_roll, reverse=True)

# The above will not work because `names` does not exist within the scope of the function.

# We can instead combine the rolls with the names using the zip() function
names_and_rolls = list(zip(names, rolls))
names_and_rolls.sort(key=lambda roll: roll[1], reverse=True)
print(names_and_rolls)
```

    ['Fred', 'Amos', 'Naomi', 'James', 'Dawes', 'Holden', 'Bobbie', 'Chrisjen']
    [('Dawes', 19), ('Fred', 18), ('Amos', 12), ('Naomi', 11), ('Bobbie', 10), ('Holden', 8), ('Chrisjen', 7), ('James', 5)]


# List Comprehensions

We can also create nested list comprehensions, which is equivalent to nested for loops. For example, let's create a 3x4 matrix using a nested list comprehension.

## Nested list comprehension

## Advanced list comprehension


```python
# Nested list comprehension

# Create a 2D list where each row represents the top 5 rolls for each person
top_rolls = [[random.randint(1, 20) for _ in range(5)] for _ in names]
print(top_rolls)

# We can create a similar 2D list where each row is a tuple of the name and the top 5 rolls
top_rolls = [(name, [random.randint(1, 20) for _ in range(5)]) for name in names]
print(top_rolls)

# If we wrote this with loops, it would look like this:
top_rolls = []
for name in names:
    rolls = []
    for _ in range(5):
        rolls.append(random.randint(1, 20))
    top_rolls.append((name, rolls))
```

    [[7, 1, 11, 15, 14], [3, 14, 15, 10, 9], [7, 16, 17, 15, 19], [12, 6, 10, 17, 19], [10, 4, 7, 17, 11], [16, 1, 14, 2, 12], [3, 10, 2, 12, 13], [7, 17, 16, 3, 6]]
    [('Fred', [15, 7, 1, 3, 16]), ('Amos', [7, 15, 9, 4, 6]), ('Naomi', [19, 7, 12, 5, 6]), ('James', [6, 11, 4, 10, 17]), ('Dawes', [13, 5, 15, 19, 8]), ('Holden', [14, 18, 16, 5, 15]), ('Bobbie', [12, 15, 8, 18, 20]), ('Chrisjen', [18, 16, 19, 10, 11])]


# Performance of list comprehensions versus `for` loops

A strong argument for list comprehensions is that they are more elegant and easier to read. However, they are also faster than for loops. Let's compare the performance of list comprehensions and for loops.

Two common benchmarks to test their performance are to append numbers to a list and to square numbers. Let's compare the performance of list comprehensions and for loops for these two tasks.


```python
import timeit

# Benchmark #1: Append vs. List Comprehension
# Append
def for_append():
    names = []
    for i in range(1000000):
        names.append(i)

# print the average out of 10 runs (in milliseconds)
print("Append: " + str(timeit.timeit(for_append, number=10) * 1000))

# List Comprehension
def list_comprehension():
    names = [i for i in range(1000000)]

# print the average out of 10 runs (in milliseconds)
print("Append: " + str(timeit.timeit(for_append, number=10) * 1000))
```

    Append: 371.44755799999984
    Append: 351.0218179999356



```python
# Benchmark 2: Squaring Numbers

# For loop
def for_loop():
    squares = []
    for i in range(1000000):
        squares.append(i**2)

# print the average out of 10 runs (in milliseconds)
print("For Loop: " + str(timeit.timeit(for_loop, number=10) * 1000))

# List Comprehension
def list_comprehension():
    squares = [i**2 for i in range(1000000)]

# print the average out of 10 runs (in milliseconds)
print("List Comprehension: " + str(timeit.timeit(list_comprehension, number=10) * 1000))
```

    For Loop: 593.4785219997138
    List Comprehension: 572.2285600004398

