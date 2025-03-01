# Python Level 1: Introduction to Python for Scientific Computing

## Introduction 

### Course Goals
This course is designed to provide a **hands-on introduction to Python** for PhD students in all scientific fields. Our goal is to help you:
- **Learn Python basics** – syntax, functions, and control structures  
- **Basic use of Python for scientific computing** – working with **NumPy** & **Matplotlib**  
- **Work in a structured way** – organizing projects, using virtual environments  
- **Write better, reusable code** – using packaging, documentation, and testing, even at (or in particular at) beginner level it makes a difference.

### **How We’ll Work**
- **Practical Approach**: We’ll alternate between short explanations and hands-on coding.  
- **Interactive Learning**: You’ll be encouraged to **ask questions** and **experiment** with the code.

All the course material is available on GitHub. You can download it and follow along, or use it as a reference later.
We will not cover all the material in the course, but we will provide you with the tools to continue learning on your own.
And the material do not cover exhaustively any of the topics, far from it, the idea is the opposite, to compile the most important concepts and tools to get you on the right track.
After that, you can dive deeper into the topics that interest you the most or that are most useful for your research using google, stackoverflow, the official documentation of the tools or your favorite IA.

## [Install Party](0_install_party/README.md)
- Install Miniforge 
- Introduction to environments with conda
- Create a Python environment with Jupyter
- JupyterLab first steps

## [Python Fundamentals](1_python_fundamentals/README.md)
- Python philosophy: The Zen of Python (`import this`).
- Basic syntax and structures: variables, data types, operators, control structures.
- Functions and modules: defining functions, importing modules.
- Object-oriented programming: classes, objects, methods.
- [Hands-on - Escape from the Matrix](1_python_fundamentals/Escaping_the_Matrix.ipynb)

## [Introduction to NumPy and Matplotlib](2_numpy_matplotlib/README.md)
- Numpy Arrays
- Basic array operations
- Basic plots with Matplotlib
- Plot Customization
- [Hands-on - Fireworks Simulation](2_numpy_matplotlib/Fireworks_Simulation.ipynb)

## [Structuring and sharing Python Projects](3_structuring_sharing/README.md)

- Code Documentation with **Docstrings**
- Code Testing with **Doctest**
- From Notebooks to Python Files
- From Python Files to Python Modules
- From Python Modules to Python Packages
- Publishing Python Packages
- [Hands-on - Escape from the Matrix with Fireworks](3_structuring_sharing/Escape_from_the_Matrix_with_Fireworks.ipynb)

## Going Further

### Collaborative Tools

The base today for collaborative work is git, a version control system that allows you to work on the same code with other people without stepping on each other's toes. It is also a great tool to keep track of your work and to go back in time if you make a mistake. We will not cover git in this course, but it is a must-have tool for any developer. You can find a lot of tutorials on the web, but I recommend the tutorial from [ARAMIS network](https://aramis.resinfo.org/) made by David Parsons:
- [slides](https://parsons.eu/git/introduction/slides.pdf)
- [tutorial](https://parsons.eu/git/introduction/hands-on.pdf)

### Python for High-Performance Computing

I recommend to start with the Gray Scoot School, a course that covers the basics of parallel computing and high-performance computing with Python but also with C, Fortran and Rust.

You can find the course material for python off the 2024 edition [here](https://gitlab.in2p3.fr/alice.faure/gray-scott-python/-/tree/main)

And check for the webinar and the next edition in 2025 [here](https://cta-lapp.pages.in2p3.fr/COURS/GRAY_SCOTT_REVOLUTIONS/GrayScottRevolution/)

### Python for Data Science

If you are interested in data science, I recommend the CNRS training: [FIDLE](https://www.fidle.cnrs.fr/w3/)
It is in french at the moment, but they are working on an english version.