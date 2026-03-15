# Sample: Python Import Examples

# Built-in module import
import math
print("math.sqrt(16):", math.sqrt(16))

# Import specific function from built-in module
from random import randint
print("randint(1, 10):", randint(1, 10))

# Import with alias
import datetime as dt
print("dt.datetime.now():", dt.datetime.now())

# User-defined module import (same package)
# Suppose you have a file named 'helper.py' in the same folder with:
# def greet(name):
#     return f"Hello, {name}!"
#
# from helper import greet
# print(greet("Alice"))

# User-defined module import (different package)
# Suppose you have a folder 'utils' with a file 'tools.py' containing:
# def add(a, b):
#     return a + b
#
# from utils.tools import add
# print(add(2, 3))

# User-defined class import (same package)
# Assumes 'helper_class.py' exists in the same folder with a 'Car' class.
from helper_class import Car
my_car = Car("Toyota", "Corolla")
print(my_car.display_info())

# Import all functions (not recommended)
# from math import *
# print(sqrt(25))

# Relative import (inside packages)
# from .helper import greet
# from ..utils.tools import add

# Note: For user-defined imports, files/folders must exist and __init__.py may be needed in packages.

# User-defined class import (from sub-package)
# Assumes 'utils/tools.py' exists with a 'Calculator' class.
from utils.tools import Calculator
calc = Calculator()
print("3 + 5 =", calc.add(3, 5))
print("4 * 6 =", Calculator.multiply(4, 6))
print("10 / 2 =", Calculator.divide(10, 2))
