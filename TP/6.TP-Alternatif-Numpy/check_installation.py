import platform
import os
print("Python version:", platform.python_version())

try:
    import numpy
    print('Module numpy:', numpy.__version__)
except ModuleNotFoundError as e:
    print(e)

try:
    import scipy
    print('Module scipy:', scipy.__version__)
except ModuleNotFoundError as e:
    print(e)

try:
    import matplotlib
    print('Module matplotlib:', matplotlib.__version__)
except ModuleNotFoundError as e:
    print(e)

try:
    import tkinter
    print('Module tkinter détecté')
except ModuleNotFoundError as e:
    print(e)

print('Installation anaconda/environnements:')
os.system("conda env list")
