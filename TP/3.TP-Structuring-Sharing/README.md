# Structuring and Sharing Python Projects: (very very) basic introduction

## Concept of technical debt

The concept of technical debt is a metaphor that describes the long-term consequences of choosing a quick and easy solution now instead of a better solution that would take longer to implement.
The term was coined by Ward Cunningham in 1992, and it has since become a widely used concept in software development.
Just like financial debt, technical debt accumulates interest over time. The longer you wait to pay it off, the more it will cost you in the long run.

### Types of technical debt

There are several types of technical debt, including:

1. **Code debt**: This is the most common type of technical debt. It occurs when developers take shortcuts to meet deadlines or deliver features quickly. This can lead to poorly written code that is hard to maintain and extend.
2. **Design debt**: This occurs when developers make design decisions that are not optimal for the long-term health of the project. For example, they may choose a design that is easy to implement in the short term but difficult to scale or maintain.
3. **Testing debt**: This occurs when developers do not write enough tests for their code. This can lead to bugs and regressions that are hard to catch and fix.
4. **Documentation debt**: This occurs when developers do not document their code properly. This can make it hard for other developers to understand and work with the code.

### Consequences of technical debt

Technical debt can have several negative consequences, including:

1. **Increased maintenance costs**: Poorly written code is harder to maintain and extend, which can lead to higher costs in the long run.
2. **Reduced productivity**: Developers spend more time fixing bugs and working around technical debt, which can reduce their productivity.
3. **Reduced quality**: Technical debt can lead to more bugs and regressions, which can reduce the quality of the software.
4. **Reduced agility**: Technical debt can make it harder to respond to changing requirements and market conditions, which can reduce the agility of the development team.

### How to manage technical debt

Managing technical debt is an ongoing process that requires a combination of technical and organizational strategies. Some common strategies include:

1. **Code reviews**: Regular code reviews can help identify technical debt early and prevent it from accumulating.
2. **Refactoring**: Refactoring is the process of restructuring existing code without changing its external behavior. It can help reduce technical debt and improve the quality of the code.
3. **Automated testing**: Automated testing can help catch bugs and regressions early, reducing the impact of technical debt.
4. **Documentation**: Proper documentation can help reduce technical debt by making it easier for developers to understand and work with the code.
5. **Training and mentoring**: Providing training and mentoring to developers can help them avoid common pitfalls that lead to technical debt.

## Avoid Global Variables

### **Why?**
Global variables:
- Make debugging harder  
- Lead to unexpected side effects  
- Reduce modularity and reusability  

### **Example of Bad Practice**
```python
# Global variable
count = 0

def increment():
    global count
    count += 1  # Modifies the global variable
```
**Problem:** Any function can modify `count`, making debugging difficult.

### **Better Approach: Use Function Parameters**
```python
def increment(count):
    return count + 1  # Returns new value instead of modifying a global variable
```
**Always prefer passing values explicitly instead of modifying global state.**

## Code Documentation with Docstrings
A **docstring** is a special comment at the beginning of a function, class, or module that explains what it does.

### **Example**
```python
def add(a, b):
    """Returns the sum of two numbers a and b."""
    return a + b
```

**Docstrings help** with readability and **autogenerate documentation**.

There are several tools to generate documentation from docstrings, such as **Sphinx** and **Doxygen**.
We will not cover them here, but you can find more information in the official documentation.

In any case, **writing docstrings is a good practice** and if you do, the way to generate the documentation is just a detail.

Keep in mind that each time you're not describing what you are doing, you are creating technical debt.

## Code Testing

### **Why Test?**

- **Ensures correctness**: Tests verify that your code works as expected.
- **Facilitates refactoring**: You can make changes with confidence.
- **Saves time**: Catch bugs early and avoid manual testing.

As for the documentation, there are several tools to write tests in Python, such as **unittest**, **pytest**, and **Doctest**.
Here we will said a few words about **Doctest** because it is simple and easy to use.

### **Doctest**

Doctest allows you to **write tests inside docstrings**.

### **Example**
```python
def square(x):
    """
    Returns the square of x.

    >>> square(3)
    9
    >>> square(-2)
    4
    """
    return x * x

if __name__ == "__main__":
    import doctest
    doctest.testmod()
```
**Run tests by executing the script**. If tests fail, it reports inconsistencies.

Doctest can be used to both document your function examples and test them at the same time.

Doctest can also be run from the command line with the `-m` flag:
```bash
python -m doctest my_module.py
```

## From Notebooks to Python Packages

Jupyter Notebooks (`.ipynb`) are great for interactive development, but for **modularity** and **reusability**, code should be converted into Python scripts.

### Convert a Jupyter Notebook to a Python File
```bash
jupyter nbconvert --to script my_notebook.ipynb
```
**Best practice**: Keep notebooks for experimentation and use `.py` files for actual project code.

If general, this is not a good practice, because the notebook is not supposed to be a script, but a document that explains the script.
It could help to start but keep in mind that you'll have to refactor the code to make it more modular and reusable.

A better approach in general is to write the code in a `.py` file from the beginning, and use the notebook to explain the code.

### Python Files 

A python file can be both a python script and a python module:
- A script is a file that is meant to be executed.
- A module is a file that is meant to be imported.

You usually have a `if __name__ == "__main__":` block at the end of the file to execute the script when it is called from the command line.
This block is not executed when the file is imported as a module.

Also at the beginning of the file, you can have a comment with the binary path to the python interpreter that should be used to execute the script.
```python
#!/usr/bin/env python
```
If the file is executable, you can run it from the command line without calling the python interpreter explicitly.

####  **Example**
```python
#!/usr/bin/env python

# my_module.py
def greet(name):
    """Returns a greeting message."""
    return f"Hello, {name}!"

if __name__ == "__main__":
    print(greet("Alice"))
```

Use it in another script:
```python
from my_module import greet

print(greet("Alice"))
```

Use it from the command line with your python interpreter:
```bash
python my_module.py
```

Use it from the command line as an executable:
```bash
chmod +x my_module.py
./my_module.py
```

### Python Packages
A **package** is a collection of **modules** in a directory with an **`__init__.py`** file.

### **Project Structure**
```
my_project/
│── my_package/
│   ├── __init__.py   # Marks it as a package
│   ├── module1.py
│   ├── module2.py
│── main.py
```
### **Example `__init__.py`**
```python
from .module1 import greet
```
**Packages allow you to organize large projects**.

### Sharing your Python Packages

Before sharing your package, you need to create a `pyproject.toml` file to describe your project and its dependencies.
`project.toml` is a very simple and efficient way to describe your project and its dependencies.
Packaging is not mandatory, but it is a good practice to have it.

The `project.toml` approach is the new standard for packaging in Python, and it is recommended to use it.
Please stop using `setup.py` and `requirements.txt` files, they are deprecated.

#### **Step 1: Create `pyproject.toml`**
```toml
[build-system]
requires = ["setuptools"]
build-backend = "setuptools.build_meta"

[project]
name = "my_package"
version = "0.1.0"
description = "A simple example package"
authors = [{name = "Your Name", email = "your@email.com"}]
dependencies = []
```

#### **Step 2: Build the Package**
```bash
pip install build
python -m build
```

#### **Step 3: Share the Package**

There are several ways to share your package:
- **GitHub**: You can share your package on GitHub by creating a repository (recommended).
- **Upload to PyPI**: The Python Package Index is the official repository for Python packages (for public packages).
- For private packages, you can use a private repository for your organization and share your package there.
- Manually share the `.tar.gz` file generated by the build command. (not recommended)

