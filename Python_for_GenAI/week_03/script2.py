"""
Python Practical Basics
========================

Topics covered:
1. Virtual Environment
2. Installing packages with pip
3. Importing modules
4. Creating reusable modules/functions
5. Introduction to Multithreading

NOTE:
The virtual environment and pip commands are written as comments
because they are executed in the terminal, not inside Python.
"""


# ============================================================
# 1. VIRTUAL ENVIRONMENT
# ============================================================

"""
Create a virtual environment in the TERMINAL:

Windows:
    python -m venv venv
    venv\Scripts\activate

Linux / macOS:
    python3 -m venv venv
    source venv/bin/activate

A virtual environment keeps this project's packages
separate from other Python projects.
"""


# ============================================================
# 2. INSTALLING PACKAGES USING PIP
# ============================================================

"""
After activating the virtual environment, run:

    python -m pip install --upgrade pip

Install an external package:

    pip install requests

Check installed packages:

    pip list

Save project dependencies:

    pip freeze > requirements.txt

Install dependencies later:

    pip install -r requirements.txt
"""


# ============================================================
# 3. IMPORTING MODULES
# ============================================================

# 'math' is a built-in Python module.
# We can import it and use its functions.

import math

print("Square root of 25:", math.sqrt(25))
print("Value of PI:", math.pi)


# 'time' is another built-in Python module.
# We will use it later for multithreading.

import time


# 'threading' is a built-in module for creating threads.

import threading


# ============================================================
# 4. CREATING REUSABLE FUNCTIONS
# ============================================================

"""
A function is a reusable block of code.

Instead of writing the same calculation again and again,
we create a function once and call it whenever needed.
"""


def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def subtract(a, b):
    """Return the difference between two numbers."""
    return a - b


def multiply(a, b):
    """Return the multiplication of two numbers."""
    return a * b


def divide(a, b):
    """
    Divide two numbers.

    We check whether b is zero before dividing
    because division by zero causes an error.
    """

    if b == 0:
        return "Cannot divide by zero."

    return a / b


# ============================================================
# 5. USING OUR REUSABLE FUNCTIONS
# ============================================================

print("\n========== REUSABLE FUNCTIONS ==========")

x = 20
y = 5

print("Addition:", add(x, y))
print("Subtraction:", subtract(x, y))
print("Multiplication:", multiply(x, y))
print("Division:", divide(x, y))


# ============================================================
# 6. ANOTHER EXAMPLE OF A REUSABLE FUNCTION
# ============================================================

def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.

    Example:
        [80, 90, 70]
        Average = 80
    """

    if len(numbers) == 0:
        return 0

    return sum(numbers) / len(numbers)


marks = [80, 85, 90, 75, 95]

average = calculate_average(marks)

print("\nMarks:", marks)
print("Average:", average)


# ============================================================
# 7. BASIC MULTITHREADING
# ============================================================

"""
Multithreading allows multiple tasks to run concurrently.

A thread can be useful for tasks such as:

- API requests
- Downloading files
- Reading files
- Waiting for network responses
- Other I/O operations

Python provides the 'threading' module for this.
"""


# ------------------------------------------------------------
# Function that will be executed by a thread
# ------------------------------------------------------------

def download_file(file_name):
    """
    Simulate downloading a file.

    time.sleep() is used here to simulate a slow operation.
    """

    print(f"{file_name}: Download started")

    # Simulate a 3-second download.
    time.sleep(3)

    print(f"{file_name}: Download completed")


# ============================================================
# 8. RUNNING WITHOUT THREADS
# ============================================================

print("\n========== WITHOUT MULTITHREADING ==========")

start_time = time.time()

# Task 1 runs first.
download_file("File 1")

# Task 2 starts only after Task 1 finishes.
download_file("File 2")

end_time = time.time()

print("Total time:",
      round(end_time - start_time, 2),
      "seconds")


# ============================================================
# 9. RUNNING WITH THREADS
# ============================================================

print("\n========== WITH MULTITHREADING ==========")

start_time = time.time()

# Create Thread 1.
thread1 = threading.Thread(
    target=download_file,
    args=("File 1",)
)

# Create Thread 2.
thread2 = threading.Thread(
    target=download_file,
    args=("File 2",)
)


# ------------------------------------------------------------
# Start both threads
# ------------------------------------------------------------

# Thread 1 starts working.
thread1.start()

# Thread 2 starts working.
thread2.start()


# ============================================================
# 10. WAIT FOR THREADS TO FINISH
# ============================================================

"""
join() tells the main program:

"Wait until this thread has finished."

Without join(), the main program may continue
before the threads complete their work.
"""

thread1.join()
thread2.join()


end_time = time.time()

print("Total time:",
      round(end_time - start_time, 2),
      "seconds")


# ============================================================
# 11. IMPORTANT CONCEPT
# ============================================================

"""
WITHOUT THREADS:

File 1 → 3 seconds
File 2 → 3 seconds

Total ≈ 6 seconds


WITH THREADS:

File 1 ─┐
        ├── running concurrently
File 2 ─┘

Total ≈ 3 seconds


This is why threading can be useful for I/O-bound tasks.
"""


print("\n========== PROGRAM FINISHED ==========")