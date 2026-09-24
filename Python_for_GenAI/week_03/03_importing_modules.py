"""
03_importing_modules.py

Topic:
Importing Python modules.
"""

# ------------------------------------------------------------
# IMPORT A BUILT-IN MODULE
# ------------------------------------------------------------

import math

print("PI:", math.pi)
print("Square root:", math.sqrt(25))


# ------------------------------------------------------------
# IMPORT SPECIFIC FUNCTION
# ------------------------------------------------------------

from math import sqrt

print("Square root:", sqrt(100))


# ------------------------------------------------------------
# IMPORT WITH AN ALIAS
# ------------------------------------------------------------

import datetime as dt

current_time = dt.datetime.now()

print("Current date and time:", current_time)