# Introduction to NumPy and Matplotlib

In this section, we'll introduce two fundamental Python libraries for scientific computing:
- **NumPy** for numerical computing.
- **Matplotlib** for data visualization.

## NumPy Basics

### What is NumPy?

NumPy (**Numerical Python**) is a **fundamental package** for numerical computing in Python.
It provides:
- **Multidimensional arrays** (faster and more memory-efficient than lists).
- **Mathematical functions** optimized for performance.
- **Operations on large datasets** used in data science, machine learning, and scientific computing.

To use NumPy, we first need to import it:
"""
import numpy as np
"""

### NumPy Arrays

The core of NumPy is the **ndarray** (n-dimensional array).
Unlike Python lists, NumPy arrays:
- Are **faster** and more memory-efficient.  
- Support **vectorized operations** (applying operations to whole arrays at once).  
- Offer **many built-in mathematical functions**.

#### Creating Arrays

You can create NumPy arrays in several ways:
"""
# Creating an array from a Python list
list_data = [1, 2, 3, 4, 5]
array_1d = np.array(list_data)
print("1D NumPy Array:", array_1d)

# Creating a 2D array (Matrix)
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("2D NumPy Array:\n", array_2d)

# Creating arrays filled with zeros or ones
zeros = np.zeros((3, 3))  # 3x3 matrix of zeros
ones = np.ones((2, 4))  # 2x4 matrix of ones

print("Zeros Array:\n", zeros)
print("Ones Array:\n", ones)

# Creating an array with a range of numbers
range_array = np.arange(0, 10, 2)  # Start at 0, go up to 10, step by 2
print("Range Array:", range_array)

# Creating an array of equally spaced values
linspace_array = np.linspace(0, 1, 5)  # 5 values from 0 to 1
print("Linspace Array:", linspace_array)
"""

### Basic Array Operations

NumPy allows **fast element-wise operations** without the need for loops.
"""
# Element-wise addition, subtraction, multiplication, and division
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("Addition:", a + b)  # [5, 7, 9]
print("Subtraction:", a - b)  # [-3, -3, -3]
print("Multiplication:", a * b)  # [4, 10, 18]
print("Division:", a / b)  # [0.25, 0.4, 0.5]

# Scalar operations
print("Multiply by Scalar:", a * 3)  # [3, 6, 9]
"""

#### Mathematical Functions
NumPy provides optimized **mathematical functions** that work on arrays.
"""
# Square root, exponential, and logarithm
print("Square Root:", np.sqrt(a))  # [1. 1.414 1.732]
print("Exponential:", np.exp(a))  # [e^1, e^2, e^3]
print("Logarithm:", np.log(a))  # Natural log
"""

#### Aggregation Functions
NumPy provides functions to compute statistics on arrays.
"""
array = np.array([[1, 2, 3], [4, 5, 6]])

print("Sum:", np.sum(array))  # Total sum of all elements
print("Mean:", np.mean(array))  # Average value
print("Max:", np.max(array))  # Largest element
print("Min:", np.min(array))  # Smallest element
print("Standard Deviation:", np.std(array))  # Measure of spread
"""

#### Indexing and Slicing
You can **access elements, rows, and slices** of a NumPy array just like Python lists.
"""
# Indexing a 1D array
arr = np.array([10, 20, 30, 40])
print("First element:", arr[0])  # 10
print("Last element:", arr[-1])  # 40

# Indexing a 2D array (matrix)
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print("Element at row 0, column 1:", matrix[0, 1])  # 2

# Slicing (extracting parts of an array)
print("First two elements:", arr[:2])  # [10, 20]
print("Last two elements:", arr[-2:])  # [30, 40]
print("First row of matrix:", matrix[0, :])  # [1, 2, 3]
"""

### Summary of Key NumPy Features

| Feature | Example |
|---------|---------|
| **Creating an Array** | `np.array([1, 2, 3])` |
| **Zeros & Ones** | `np.zeros((3,3))`, `np.ones((2,4))` |
| **Range of Numbers** | `np.arange(0, 10, 2)`, `np.linspace(0, 1, 5)` |
| **Element-wise Math** | `a + b`, `a * 3`, `np.sqrt(a)`, `np.log(a)` |
| **Aggregation** | `np.sum(a)`, `np.mean(a)`, `np.max(a)`, `np.std(a)` |
| **Indexing** | `a[0]`, `matrix[1,2]` |
| **Slicing** | `a[:2]`, `matrix[:,1]` |

To learn more about NumPy, check out the [official documentation](https://numpy.org/doc/stable/).

## Matplotlib Basics

Matplotlib is a **Python library for data visualization**. It is widely used for **plotting graphs, animations, and interactive visualizations**.   

### Creating Basic Plots
```python
import matplotlib.pyplot as plt  
import numpy as np  

# Create sample data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Plot the data
plt.plot(x, y, label="Sine Wave", color="blue")

# Add labels and title
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Basic Plot")

# Show legend and grid
plt.legend()
plt.grid(True)

# Display the plot
plt.show()
```

### Scatter Plots 
Scatter plots are useful for displaying individual points.  
```python
# Generate random particle positions
x = np.random.uniform(-5, 5, 100)
y = np.random.uniform(-5, 5, 100)

plt.scatter(x, y, color="red", alpha=0.7)  # Scatter plot with transparency
plt.xlabel("X Position")
plt.ylabel("Y Position")
plt.title("Particle Positions")

plt.show()
```

### Creating a Color Map (`imshow()`) 
`imshow()` allows you to visualize **density distributions** in a **2D space**.  
```python
# Create random density map
density = np.random.rand(10, 10)

plt.imshow(density, cmap="inferno", origin="lower")  # Inferno color scheme for heatmaps
plt.colorbar(label="Particle Density")
plt.title("Heatmap of Particle Distribution")

plt.show()
```

### Creating Animations (`FuncAnimation`)
```python
from matplotlib.animation import FuncAnimation  

fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
particles, = ax.plot([], [], "ro")  # Red particles

# Generate initial particle positions
num_particles = 50
x = np.zeros(num_particles)
y = np.zeros(num_particles)
vx = np.random.uniform(-1, 1, num_particles)
vy = np.random.uniform(-1, 1, num_particles)

def update(frame):
    global x, y
    x += vx * 0.1  # Update positions
    y += vy * 0.1
    particles.set_data(x, y)
    return particles,

# Create animation
ani = FuncAnimation(fig, update, frames=100, interval=50)
plt.show()
```

## Scipy Basics

SciPy (**Scientific Python**) is a powerful **open-source** library built on **NumPy**, providing advanced **scientific computing** functions. It is widely used for **optimization, signal processing, statistics, linear algebra, and more**.

If NumPy provides **basic numerical operations**, SciPy extends it with **higher-level mathematical tools**.

### Special Functions (`scipy.special`)
SciPy includes **many mathematical functions**, such as:
- Gamma (`gamma`), Beta (`beta`), and Bessel (`jn`, `yn`) functions.
- Error function (`erf`), which is useful in probability and statistics.

```python
from scipy.special import gamma, erf

print(gamma(5))  # Factorial of 4 → Output: 24
print(erf(1.0))  # Error function at x=1 → Output: 0.8427
```

### Linear Algebra (`scipy.linalg`)**
SciPy extends NumPy’s `linalg` with:
- **Matrix decomposition** (LU, QR, SVD)
- **Eigenvalue computations**
- **Solving linear systems of equations**

```python
import numpy as np
from scipy.linalg import lu, svd

A = np.array([[3, 2], [1, 4]])

# LU decomposition
P, L, U = lu(A)
print("Lower Matrix:\n", L)
print("Upper Matrix:\n", U)

# Singular Value Decomposition (SVD)
U, s, Vh = svd(A)
print("Singular values:", s)
```

### Optimization (`scipy.optimize`)
Used for **minimization problems**, such as:
- **Finding function minima/maxima**
- **Root finding**
- **Curve fitting**

```python
from scipy.optimize import minimize

# Function to minimize (example: f(x) = x² + 5x + 6)
def func(x):
    return x**2 + 5*x + 6

result = minimize(func, x0=0)  # Start search at x=0
print("Optimal x:", result.x)
```

### Statistics & Probability (`scipy.stats`)
SciPy provides **advanced statistical functions**, such as:
- Probability distributions (**normal, binomial, Poisson**)
- Hypothesis testing (**t-test, chi-square**)
- Random sampling

```python
from scipy.stats import norm

# Generate random values from a normal distribution
samples = norm.rvs(loc=0, scale=1, size=10)
print("Random samples:", samples)

# Compute probability density function (PDF) at x=0
print("PDF at x=0:", norm.pdf(0))
```

### Signal Processing (`scipy.signal`)
SciPy supports:
- **Fourier Transforms** (`scipy.fft`)
- **Filtering & Smoothing** (`butter`, `filtfilt`)
- **Convolution** (`convolve`)

```python
from scipy.signal import butter, filtfilt

# Create a low-pass filter
b, a = butter(N=3, Wn=0.1, btype='low')
filtered_signal = filtfilt(b, a, np.sin(np.linspace(0, 10, 100)))
```
