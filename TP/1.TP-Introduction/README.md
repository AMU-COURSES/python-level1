# Python Fundamentals

This material cover the minimum Python knowledge required to abort this course.
For complete list of Python features and syntax, check out the [Python Documentation](https://docs.python.org/).

## Python Philosophy: The Zen of Python  

Python is designed to be **readable, simple, and elegant**. You can view its guiding principles by running:

```python
import this
```

You'll see **"The Zen of Python"**, which includes principles like:  
- **Readability counts.**
- **Simple is better than complex.** 
- **There should be one**—and preferably only one—**obvious way to do it.**

Python encourages **clean, readable, and maintainable** code.

## Basic Syntax and Structures  

### Variables and Data Types

Python is **dynamically typed**, meaning you don’t need to specify types explicitly.

```python
# Common data types
x = 10          # Integer
y = 3.14        # Float
name = "Alice"  # String
is_happy = True # Boolean
fruits = ["apple", "banana", "cherry"] # List
```

### Operators

Python supports standard **arithmetic, comparison, and logical operators**.

```python
# Arithmetic Operators
a = 10 + 5  # Addition
b = 10 - 5  # Subtraction
c = 10 * 5  # Multiplication
d = 10 / 3  # Division (returns float)
e = 10 // 3 # Floor division (returns int)
f = 10 % 3  # Modulo (remainder)
g = 2 ** 3  # Exponentiation (2^3)

# Comparison Operators
x == y  # Equal
x != y  # Not equal
x > y   # Greater than
x < y   # Less than
x >= y  # Greater than or equal to
x <= y  # Less than or equal to

# Logical Operators
a and b  # Returns True if both a and b are True
a or b   # Returns True if either a or b is True
not a    # Returns the opposite boolean value of a
```

### Strings and String Operations

```python
# String concatenation
first_name = "John"
last_name = "Doe"

full_name = first_name + " " + last_name  # Output: "John Doe"

# String formatting
name = "Alice"
greeting = f"Hello, {name}!"  # Output: "Hello, Alice!"
```

### Printing Output

```python
print("Hello, World!")
```

Print variables and expressions:

```python
x = 10
print(x)  # Output: 10

y = 20
print(x + y)  # Output: 30
```

Print multiple values:

```python
name = "Alice"
age = 30
print("Name:", name, "Age:", age)  # Output: Name: Alice Age: 30
```

### Control Structures: Conditional Statements

```python
x = 10
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is exactly 5")
else:
    print("x is less than 5")
```


### List

A **list** is a collection of items that can be of different types.

```python
fruits = ["apple", "banana", "cherry"]
print(fruits[1])  # Output: banana

numbers = [1, 2, 3, 4, 5]
print(len(numbers))  # Output: 5

# mix of data types
mixed = [1, "apple", True]
```

Python provide **list comprehension** for creating lists in a concise way.

```python
# Generate a list of squares
squares = [x**2 for x in range(5)]  # Output: [0, 1, 4, 9, 16]
```

### Loops: For and While

```python
# For loop: Iterate over a sequence
for fruit in ["apple", "banana", "cherry"]:
    print(fruit)

# While loop: Repeat until condition is met
count = 0
while count < 3:
    print("Count:", count)
    count += 1
```

## Functions and Modules

### Defining Functions

Functions allow **code reuse** and **better organization**.

```python
# Function with parameters and return value
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))  # Output: Hello, Alice!
```

### Default and Keyword Arguments

```python
def power(base, exponent=2):  # Default exponent is 2
    return base ** exponent

print(power(3))     # Output: 9 (3²)
print(power(3, 3))  # Output: 27 (3³)
```

### Importing Modules

Python has a **rich standard library**.

```python
import math
print(math.sqrt(16))  # Output: 4.0
```

You can also **import specific functions**:

```python
from math import pi, sin
print(pi)  # Output: 3.141592653589793
```

You can **import modules with an alias**:

```python
import math as m
print(m.sqrt(16))  # Output: 4.0
```

## Dictionaries

A **dictionary** is a collection of key-value pairs.

```python
person = {
    "name": "Alice",
    "age": 30,
    "is_happy": True
}

print(person["name"])  # Output: Alice
```

### Dictionary Comprehension

```python
# Generate a dictionary of squares
squares = {x: x**2 for x in range(5)}  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

## Tuples

A **tuple** is an immutable collection of items.

```python
point = (10, 20)
print(point[0])  # Output: 10
```

Immutable means you can't change the values of a tuple after it's created.
```python
point[0] = 20  # Error: 'tuple' object does not support item assignment
```

## Random Numbers

Python provides a **random module** to generate random numbers.

```python
import random

# Generate a random integer
random_int = random.randint(1, 10)  # Random integer between 1 and 10
print(random_int)

# Generate a random float
random_float = random.uniform(1, 10)  # Random float between 1 and 10
print(random_float)
```

## Object-Oriented Programming

Python supports **Object-Oriented Programming**, allowing you to define **classes and objects**.

In a nutshell, Object-Oriented Programming is a programming paradigm that uses objects to model real-world data and behavior.
In theory, it helps you to organize your code and make it more reusable and maintainable.
In practice, you have to be careful to not over-engineer your code.

### Defining a Class

```python
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def speak(self):
        return f"{self.name} makes a sound."

# Creating objects
dog = Animal("Buddy", "Dog")
cat = Animal("Whiskers", "Cat")

print(dog.speak())  # Output: Buddy makes a sound.
```

### Class Inheritance

Child classes can inherit from a parent class and extend or override behavior.

```python
class Dog(Animal):  # Dog class inherits from Animal
    def speak(self):
        return f"{self.name} barks!"

class Cat(Animal):  
    def speak(self):
        return f"{self.name} meows!"

dog = Dog("Rex", "Dog")
cat = Cat("Luna", "Cat")

print(dog.speak())  # Output: Rex barks!
print(cat.speak())  # Output: Luna meows!
```

### Beginners advice about Object-Oriented Programming

- **Keep it simple!**
- Use Object to group related data and functions
- In the context of scientific computing, inehritance is not necessary in most cases, so keep it simple.
