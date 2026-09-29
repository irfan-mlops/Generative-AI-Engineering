# A function is a reusable block of code designed to perform a specific task.
# We define a function using the 'def' keyword.

def greet():
    # This statement prints a greeting message when the function is called.
    print("Hello, welcome to Python!")


# Calling the function to execute the code inside it.
greet()

#=====================================================================
# This is a parameterized function because it accepts a parameter.
# 'name' is a parameter that acts as a placeholder for a value.

def greet(name): # Parameter 
    # Print the value received through the 'name' parameter.
    print("Hello", name)


# Calling the function and passing "Irfan" as an argument.
greet("Irfan") # Actual Argument

# Calling the same function with a different argument.
greet("Ahmed") # Actual Argument 

#====================================================================

# Define a function with two parameters.
# 'name' and 'age' are parameters because they are defined in the function definition.

def introduce(name, age):
    # Print the value received through the 'name' parameter.
    print("Name:", name)

    # Print the value received through the 'age' parameter.
    print("Age:", age)


# "Irfan" and 25 are actual arguments because they are the
# actual values passed to the function during the function call.
introduce("Kim ", 25)

#====================================================================

# A function saves us from writing the same code again and again.
# We can use a function whenever we need to do the same task.
# Functions make our code more organized.
# Functions make it easier to work with large programs.

#====================================================================

# print() is used to display something on the screen.
print("Hello World")

# len() is used to find the length of a value.
print(len("Python"))

# type() is used to check the data type of a value.
print(type(10))

# max() is used to find the largest value.
print(max(10, 20, 30))

# min() is used to find the smallest value.
print(min(10, 20, 30))

# sum() is used to calculate the total of numbers.
print(sum([10, 20, 30]))

# abs() is used to get the positive value of a number.
print(abs(-10))

# round() is used to round a number.
print(round(3.567))

# Common built-in functions: print(), len(), type(), max(), min(), sum(), abs(), round(), input(), int(), float(), str().

# These functions are already provided by Python, so we don't need to define them ourselves.