"""Calculator. To use complex functions, see the math module documentation."""

from math import *
from typing import Union


def ctg(value: Union[int, float]) -> float:
    """Return the tangent of x (measured in radians)."""
    return cos(value) / sin(value)


def tg(value: Union[int, float]) -> float:
    """Return the cotangent of x (measured in radians)."""
    return sin(value) / cos(value)


def calculator(expression: str) -> Union[int, float, str]:
    """Returns the result of executing a mathematical expression."""
    try:
        result = eval(str(expression))
        return result
    except (SyntaxError, NameError, ZeroDivisionError, ValueError):
        return "Error! Incorrect expression"


# Comment out the code below before unit tests

"""print("Welcome to the best calculator! If you want to use trigonometric "
      "functions and enter angles in radians, then use radians(x), where x is your angle. "
      "For example sin(radians(45)), tg(radians(90))")
while True:
    received_expression = input("Enter an expression or '-1' to exit: ")
    if received_expression == "-1":
        print("The work is completed")
        break
    print(calculator(received_expression))"""
