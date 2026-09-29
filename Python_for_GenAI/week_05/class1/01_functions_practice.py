"""
Problem 1 — Greeting Function

Problem Statement

Write a Python function named greet_user that displays a welcome message to the user.

Function Requirements

Function name: greet_user
Parameters: None
The function should print the following message:
"Hello, welcome to Python!"
Call the function to verify that it works correctly.
Do not use a return statement.

Example

Function Call:

greet_user()

Expected Output:

Hello, welcome to Python!

Concepts Practiced

Defining a function
Calling a function
Non-parameterized function
Using print()
"""

# Solution
# Define a function that displays a welcome message.
def greet_user():
    # Print the welcome message.
    print("Hello, welcome to Python!")


# Call the function to display the message.
greet_user()

#==============================================================================================

"""
Problem 2 — Display User Name

Problem Statement

Write a Python function named display_name that displays a user's name.

Function Requirements

Function name: display_name
Parameters: 1
The parameter should represent the user's name.
Print the user's name using the parameter.
Call the function with the name "Jeon Wik".
Do not use a return statement.

Example

Function Call:
display_name("Jeon Wik")

Expected Output:
Name: Jeon  Wik

Concepts Practiced

Defining a function
Parameterized function
Parameter
Actual argument
Function call
print() 
"""

# Define a function that displays a user's name.
def display_name(name):
    # Print the name received through the parameter.
    print(name)


# Call the function and pass a name as an actual argument.
display_name("Jeon wik")

#=======================================================================
"""
Problem 3 — Calculate Rectangle Area
Problem Statement

Write a Python function named calculate_rectangle_area that calculates and displays the area of a rectangle.

Function Requirements
Function name: calculate_rectangle_area
Parameters: 2
The first parameter should represent the rectangle's length.
The second parameter should represent the rectangle's width.
Calculate the area using:
Area = Length × Width
Display the calculated area using print().
Call the function with any valid length and width of your choice.
Do not use a return statement.

"""

# Define a function to calculate the area of a rectangle.
def calculate_rectangle_area(length, width):
    # Calculate the area using length × width.
    area = length * width

    # Display the calculated area.
    print("Rectangle Area:", area)


# Call the function with length and width as actual arguments.
calculate_rectangle_area(20, 30)

#===================================================================================
"""
Problem 4 — Calculate Total and Average
Problem Statement

Write a Python function named calculate_result that accepts three subject marks and calculates both the total marks and the average marks.

Function Requirements
Function name: calculate_result
Parameters: 3
The parameters should represent three subject marks.
Calculate the total of the three marks.
Calculate the average of the three marks.
Display both the total and average.
Call the function with any three marks of your choice.
Do not use a return statement.

"""

# Define a function to calculate total and average marks.
def calculate_results(math, chemistry, biology):

    # Calculate the total marks of all three subjects.
    total_marks = math + chemistry + biology

    # Calculate the average marks.
    average_marks = total_marks / 3

    # Display the total marks.
    print("Total Marks:", total_marks)

    # Display the average marks.
    print("Average Marks:", average_marks)


# Call the function with actual marks for each subject.
calculate_results(80, 100, 50)

#============================================================================================
"""
Problem 5 — Check Even or Odd

Ab thora aur difficult karte hain. Is baar parameter + condition (if/else) use karni hai.

Problem Statement

Write a Python function named check_number that determines whether a given number is even or odd.

Function Requirements
Function name: check_number
Parameters: 1
The parameter should represent a number.
If the number is divisible by 2, display:
Even Number
Otherwise, display:
Odd Number
Call the function with any number of your choice.
Do not use a return statement. 

"""

# Define a function to check whether a number is even or odd.
def check_number(n):

    # Check whether the number is divisible by 2.
    if n % 2 == 0:
        print(f"{n} is an Even Number")

    # If the number is not divisible by 2, it is odd.
    else:
        print(f"{n} is an Odd Number")


# Call the function with an actual argument.
check_number(21)

#========================================================================================
"""
Problem 6 — Find the Larger Number

Ab thora aur challenging.

Problem Statement

Write a Python function named find_larger that accepts two numbers and determines which number is larger.

Function Requirements
Function name: find_larger
Parameters: 2
Compare the two numbers using if/else.
If the first number is larger, display:
First number is larger
If the second number is larger, display:
Second number is larger
If both numbers are equal, display:
Both numbers are equal
Call the function with any two numbers of your choice.
Do not use a return statement.

"""

# Define a function to find the larger of two numbers.
def find_larger(num1, num2):

    # Check if the first number is greater than the second number.
    if num1 > num2:
        print(f"{num1} is greater than {num2}.")

    # Check if the second number is greater than the first number.
    elif num1 < num2:
        print(f"{num2} is greater than {num1}.")

    # If neither number is greater, both numbers are equal.
    else:
        print(f"{num1} and {num2} are equal.")


# Call the function with two actual arguments.
find_larger(10, 10)

#=================================================================


