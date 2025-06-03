# Classes

When a class is defined, a namespace is created for it. All assignments to local variables are part of this namespace. The code below defines a class, creates an instance of the class, and calls a method on the instance.


```python
class Shape():
    """Represents any shape."""
    def __init__(self, color):
        self.color = color
        self.orientation = 0.0

    def rotate(self, angle):
        self.orientation += angle

s = Shape("red")
s.rotate(45.0)
print(s.orientation)
```

    45.0


## Class and Instance Variables

The class above has two *instance* variables, `color` and `orientation`. These variables are accessed using the `self` keyword. The `self` keyword is used to access instance variables and methods.

Classes can also have *class* variables that are accessible, and shared, by all instances of the class. Let's add a class variable to the `Shape` class.

### Private Variables

Python does not have a formal mechanism for describing a private variable. You can still create them using naming conventions. A common approach to creating private variables is to prefix each identifier with double underscores. If we wanted to make the `orientation` variable private, we would rename it to `__orientation`, for example.


```python
class Shape():
    """Represents any shape."""

    max_area = 100.0

    def __init__(self, color):
        self.color = color
        self.orientation = 0.0

    def rotate(self, angle):
        self.orientation += angle

s = Shape("red")
s.rotate(45.0)
r = Shape("blue")
print(s.orientation)
print("Maximum area for a shape:", Shape.max_area)
```

    45.0
    Maximum area for a shape: 100.0


# Special Methods

We already saw one special method, `__init__()`, that serves as our constructor for a class. There are several others that are useful for customizing our classes. They are
- `__str__()`: called when `str()` is called on an instance of the class
- `__repr__()`: called when `repr()` is called on an instance of the class
- `__len__()`: called when `len()` is called on an instance of the class
- `__add__()`: called when `+` is used on two instances of the class
- `__eq__()`: called when `==` is used on two instances of the class
- `__lt__()`: called when `<` is used on two instances of the class
- `__gt__()`: called when `>` is used on two instances of the class
- `__le__()`: called when `<=` is used on two instances of the class
- `__ge__()`: called when `>=` is used on two instances of the class
- `__ne__()`: called when `!=` is used on two instances of the class
- `__hash__()`: called when `hash()` is called on an instance of the class
- `__bool__()`: called when `bool()` is called on an instance of the class

Let's modify the `Shape` class to add a few of these methods. We will also add an `area` attribute so that we can override the comparison operators.


```python

class Shape():
    """Represents any shape."""

    max_area = 100.0

    def __init__(self, color, area):
        self.color = color
        self.orientation = 0.0
        self.area = area

    def rotate(self, angle):
        self.orientation += angle

    def __eq__(self, other):
        return self.area == other.area
    
    def __lt__(self, other):
        return self.area < other.area
    
    def __gt__(self, other):
        return self.area > other.area
    
    def __le__(self, other):
        return self.area <= other.area
    
    def __ge__(self, other):
        return self.area >= other.area
    
    def __ne__(self, other):
        return self.area != other.area
    
    def __str__(self):
        return "Shape, color: {0}, area: {1}".format(self.color, self.area)
    
    s1 = Shape("red", 10.0)
    s2 = Shape("blue", 20.0)
    print("s1 == s2:", s1 == s2)
    print("s1 != s2:", s1 != s2)
    print("s1 < s2:", s1 < s2)
    print("s1 > s2:", s1 > s2)
    print("s1 <= s2:", s1 <= s2)
    print("s1 >= s2:", s1 >= s2)
    print(s1)
    print(s2)
```

    s1 == s2: False
    s1 != s2: True
    s1 < s2: True
    s1 > s2: False
    s1 <= s2: True
    s1 >= s2: False
    Shape, color: red, area: 10.0
    Shape, color: blue, area: 20.0


Since we have defined the `<` operator, `list.sort()` can sort our shapes. If the `__lt__()` operator was not defined, `list.sort()` would use the `__gt__()` operator. If neither are defined, attemping to sort would result in an error. Let's add a few more and verify this.


```python
import random

colors = ["red", "blue", "green", "yellow", "black", "white"]

# Generate 10 shapes with random colors and areas
shapes = []
for i in range(10):
    color = random.choice(colors)
    area = random.uniform(0.0, 100.0)
    shapes.append(Shape(color, area))

# Print the shapes, sorted by area
for shape in sorted(shapes):
    print(shape)
```

    Shape, color: red, area: 13.697816464863
    Shape, color: white, area: 42.56718610585648
    Shape, color: white, area: 47.443134198872464
    Shape, color: white, area: 53.85070279838825
    Shape, color: yellow, area: 66.78631236791435
    Shape, color: green, area: 70.55065950752918
    Shape, color: blue, area: 73.19818592952365
    Shape, color: white, area: 74.03228452807117
    Shape, color: black, area: 86.72544463003362
    Shape, color: red, area: 94.59245601130148


# Inheritance

Inheritance allows us to create a specialized version of another class. Generally, this means that our specialized class has access to the methods and instance variables of the parent class. Let's create a `Circle` and `Square` that inherit from shape. Their areas will be calculated based on their properties.


```python
import math


class Shape():
    """Represents any shape."""

    max_area = 100.0

    def __init__(self, color):
        self.color = color
        self.orientation = 0.0

    def rotate(self, angle):
        self.orientation += angle

    def __eq__(self, other):
        return self.area == other.area
    
    def __lt__(self, other):
        return self.area < other.area
    
    def __gt__(self, other):
        return self.area > other.area
    
    def __le__(self, other):
        return self.area <= other.area
    
    def __ge__(self, other):
        return self.area >= other.area
    
    def __ne__(self, other):
        return self.area != other.area
    
    def __str__(self):
        return "Shape, color: {0}, area: {1}".format(self.color, self.area)

class Circle(Shape):
    """Represents a circle."""

    def __init__(self, color, radius):
        Shape.__init__(self, color)
        self.radius = radius
        self.area = self.get_area()

    def __str__(self):
        return "Circle, color: {0}, area: {1}, radius: {2}".format(self.color, self.area, self.radius)
    
    def get_area(self):
        return 2 * math.pi * self.radius ** 2
    
class Rectangle(Shape):
    """Represents a rectangle."""

    def __init__(self, color, width, height):
        Shape.__init__(self, color)
        self.width = width
        self.height = height
        self.area = self.get_area()

    def __str__(self):
        return "Rectangle, color: {0}, area: {1}, width: {2}, height: {3}".format(self.color, self.area, self.width, self.height)
    
    def get_area(self):
        return self.width * self.height
    
shape_classes = [Rectangle, Circle]
colors = ["red", "blue", "green", "yellow", "black", "white"]

# Generate 10 shapes with random colors and areas
shapes = []
for i in range(10):
    color = random.choice(colors)
    shape_class = random.choice(shape_classes)
    if shape_class == Rectangle:
        width = random.uniform(0.0, math.sqrt(Shape.max_area))
        height = random.uniform(0.0, math.sqrt(Shape.max_area))
        shape = Rectangle(color, width, height)
    else:
        radius = random.uniform(0.0, math.sqrt(Shape.max_area / (2 * math.pi)))
        shape = Circle(color, radius)
    shapes.append(shape)

# Print the shapes, sorted by area
for shape in sorted(shapes):
    print(shape)
```

    Circle, color: blue, area: 0.5110628296555956, radius: 0.2851984845159934
    Rectangle, color: yellow, area: 0.6186484099066036, width: 0.2740689854907352, height: 2.25727259433927
    Circle, color: white, area: 5.867493292628993, radius: 0.9663542627217231
    Circle, color: green, area: 18.28116762721217, radius: 1.7057368476298893
    Rectangle, color: blue, area: 20.114023003818147, width: 5.075190544004695, height: 3.963205485472614
    Rectangle, color: blue, area: 23.171307446004665, width: 2.586024349725701, height: 8.960204666465124
    Circle, color: red, area: 42.43901187799147, radius: 2.598918721375873
    Rectangle, color: white, area: 45.198912747710224, width: 9.793600740960953, height: 4.615147578833736
    Circle, color: yellow, area: 47.991651978311594, radius: 2.7637128359318064
    Rectangle, color: green, area: 83.54726788281138, width: 9.643204828660805, height: 8.66384872739595


## `global` and `nonlocal` keywords

The `global` keyword is used to declare an identifier that can be used for the entire code block. This is useful when we want to use a variable in a function that is defined outside of the function.



```python
x = 1

def f():
    global x # global keyword is used to access a global variable from a function
    x = 2

f()
print(x)
```

    2


The `nonlocal` keyword is used to declare an identifier that is defined in the nearest enclosing scope. This is useful when we want to use a variable in a nested function that is defined outside of the nested function. 



```python
def f():
    x = 1
    def g():
        nonlocal x
        x = 2
    g()
    print(x)
f()
```

    2


The following example from [the official Python docs](https://docs.python.org/3/tutorial/classes.html) shows the relationship between global, local, and nonlocal variables.


```python
def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)
```

    After local assignment: test spam
    After nonlocal assignment: nonlocal spam
    After global assignment: nonlocal spam
    In global scope: global spam


The unexpected result here is that `spam` is still equal to `nonlocal` even though it was changed in `do_global` by declaring `global spam`. When declaring something as `nonlocal`, the variable must already exist in the enclosing namespace. The declaration of `global spam` created a new instance of `spam` in the `global` namespace.

The example below shows how local, nonlocal, and global variables work in the context of classes.


```python
class User:
    """Represents a user."""

    def __init__(self, id, name, password):
        self.id = id
        self.name = name
        self.password = password
        self.domain = "unknown"

    def __str__(self):
        return "User: {0}, id: {1}".format(self.name, self.id)

    def global_login(self):
        global domain
        self.domain = domain

    # def nonlocal_login(self):
    #     nonlocal domain
    #     domain = "compuserve.net"

    def nonlocal_login(self):
        domain = "compuserve.net"

        def set_domain():
            nonlocal domain
            self.domain = domain

        set_domain()

    def local_login(self):
        self.domain = "tx.rr.com"

domain = "gmail.com"
u = User(1, "John", "password")
u.global_login()
print(u.domain)

u.nonlocal_login()
print(u.domain)

u.local_login()
print(u.domain)


```

    gmail.com
    compuserve.net
    tx.rr.com


# Data Classes

Sometimes in our work, we may want to represent a simple class consisting only of attributes, similar to a `struct` in C. Python provides a way to do this using the `dataclass` decorator. The `dataclass` decorator will automatically generate a constructor, `__repr__()`, and `__eq__()` method for us. The follow example shows how to implement such a class.


```python
from dataclasses import dataclass

@dataclass
class Product:
    """Represents a product."""
    id: int
    name: str
    price: float
    quantity: int = 0

    def __str__(self):
        return "Product: {0}, id: {1}".format(self.name, self.id)
    
# Let's create a list of graphics cards and list them
products = []
products.append(Product(1, "GeForce RTX 2080 Ti", 1200.0))
products.append(Product(2, "GeForce RTX 2080", 800.0))
products.append(Product(3, "GeForce RTX 2070", 600.0))
products.append(Product(4, "GeForce RTX 2060", 350.0))
products.append(Product(5, "GeForce GTX 1660 Ti", 275.0))
products.append(Product(6, "GeForce GTX 1660", 200.0))
products.append(Product(7, "GeForce GTX 1650", 150.0))
products.append(Product(8, "GeForce GTX 1080 Ti", 800.0))
products.append(Product(9, "GeForce GTX 1080", 500.0))
products.append(Product(10, "GeForce GTX 1070 Ti", 450.0))

for product in products:
    print(product)
```

    Product: GeForce RTX 2080 Ti, id: 1
    Product: GeForce RTX 2080, id: 2
    Product: GeForce RTX 2070, id: 3
    Product: GeForce RTX 2060, id: 4
    Product: GeForce GTX 1660 Ti, id: 5
    Product: GeForce GTX 1660, id: 6
    Product: GeForce GTX 1650, id: 7
    Product: GeForce GTX 1080 Ti, id: 8
    Product: GeForce GTX 1080, id: 9
    Product: GeForce GTX 1070 Ti, id: 10


# Iterators

We have used iterator objects, like a list, in previous examples. When defining our own custom classes, we can also define them as iterators. To do this, we need to implement the `__iter__()` and `__next__()` methods. The `__iter__()` method should return the iterator object itself. The `__next__()` method should return the next item in the sequence. When there are no more items in the sequence, `__next__()` should raise a `StopIteration` exception.

This will be useful for our final example, where we will implement a dataloader for a machine learning application. To illusterate iterators with a simpler example, we need to justify the need to implement our own iterator. If we create something simple that iterates over a simple list of objects, why not just use the list itself?

Let's create a class that represents a 3D object. A 3D object has a list of vertices and a list of faces. Each face is a list of indices into the list of vertices. We will create a class that represents a 3D object. Our iterator for this class will iterator over the faces of the object, returning the vertices that make up each face.


```python
class Model:
    """Represents a 3D model."""

    def __init__(self, vertices, faces):
        self.vertices = vertices
        self.faces = faces
        self.index = 0

    def __str__(self):
        return "{} vertices, {} faces".format(len(self.vertices), len(self.faces))

    def __len__(self):
        return len(self.faces)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.faces):
            raise StopIteration
        face = self.faces[self.index]
        vertices = []
        for vertex_index in face:
            vertices.append(self.vertices[vertex_index])
        self.index += 1
        return vertices
    
    def __getitem__(self, key):
        vertices = []
        for vertex_index in self.faces[key]:
            vertices.append(self.vertices[vertex_index])
        return vertices
    
# Create a cube model
vertices = [(0.0, 0.0, 0.0), (1.0, 0.0, 0.0), (1.0, 1.0, 0.0), (0.0, 1.0, 0.0),
            (0.0, 0.0, 1.0), (1.0, 0.0, 1.0), (1.0, 1.0, 1.0), (0.0, 1.0, 1.0)]
faces = [(0, 1, 2, 3), (1, 5, 6, 2), (5, 4, 7, 6), (4, 0, 3, 7), (3, 2, 6, 7), (4, 5, 1, 0)]
cube = Model(vertices, faces)

# Iterator over the model
for face in cube:
    print("Face {}: {}".format(cube.index, face))
```

    Face 1: [(0.0, 0.0, 0.0), (1.0, 0.0, 0.0), (1.0, 1.0, 0.0), (0.0, 1.0, 0.0)]
    Face 2: [(1.0, 0.0, 0.0), (1.0, 0.0, 1.0), (1.0, 1.0, 1.0), (1.0, 1.0, 0.0)]
    Face 3: [(1.0, 0.0, 1.0), (0.0, 0.0, 1.0), (0.0, 1.0, 1.0), (1.0, 1.0, 1.0)]
    Face 4: [(0.0, 0.0, 1.0), (0.0, 0.0, 0.0), (0.0, 1.0, 0.0), (0.0, 1.0, 1.0)]
    Face 5: [(0.0, 1.0, 0.0), (1.0, 1.0, 0.0), (1.0, 1.0, 1.0), (0.0, 1.0, 1.0)]
    Face 6: [(0.0, 0.0, 1.0), (1.0, 0.0, 1.0), (1.0, 0.0, 0.0), (0.0, 0.0, 0.0)]


# Generators

Generators provide a much cleaner way to implement iterators. Instead of implementing the `__iter__()` and `__next__()` methods, we can use the `yield` keyword. The `yield` keyword is used to return a value from a generator. The generator will remember its place in the sequence and return the next value when `next()` is called on it.

Since our class already included `__getitem__()`, we can use the `yield` keyword to implement our iterator.


```python
def get_next_face(model):
    for face in range(len(model)):
        yield model[face]

# Generator function
for face in get_next_face(cube):
    print(face)
```

    [(0.0, 0.0, 0.0), (1.0, 0.0, 0.0), (1.0, 1.0, 0.0), (0.0, 1.0, 0.0)]
    [(1.0, 0.0, 0.0), (1.0, 0.0, 1.0), (1.0, 1.0, 1.0), (1.0, 1.0, 0.0)]
    [(1.0, 0.0, 1.0), (0.0, 0.0, 1.0), (0.0, 1.0, 1.0), (1.0, 1.0, 1.0)]
    [(0.0, 0.0, 1.0), (0.0, 0.0, 0.0), (0.0, 1.0, 0.0), (0.0, 1.0, 1.0)]
    [(0.0, 1.0, 0.0), (1.0, 1.0, 0.0), (1.0, 1.0, 1.0), (0.0, 1.0, 1.0)]
    [(0.0, 0.0, 1.0), (1.0, 0.0, 1.0), (1.0, 0.0, 0.0), (0.0, 0.0, 0.0)]

