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

