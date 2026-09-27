"""
04_reusable_modules.py

Topic:
Creating reusable modules.

A module is simply a Python file containing reusable code.
"""

# ------------------------------------------------------------
# REUSABLE FUNCTIONS
# ------------------------------------------------------------

def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def subtract(a, b):
    """Return the difference between two numbers."""
    return a - b


def multiply(a, b):
    """Return the product of two numbers."""
    return a * b


def calculate_average(numbers):
    """Calculate the average of a list of numbers."""

    if not numbers:
        return 0

    return sum(numbers) / len(numbers)


# ------------------------------------------------------------
# TEST OUR FUNCTIONS
# ------------------------------------------------------------

print("Addition:", add(10, 5))
print("Subtraction:", subtract(10, 5))
print("Multiplication:", multiply(10, 5))

marks = [80, 90, 70, 85]

print("Average:", calculate_average(marks))


# ------------------------------------------------------------
# IMPORTANT
# ------------------------------------------------------------

"""
In a real project, this file could be imported into another file:

from reusable_modules import add, calculate_average

Then we can use:

result = add(10, 20)

This allows us to write code once
and reuse it in many places.
"""