# Topics:
# 1. Exceptions
# 2. Raising custom Exceptions
# 3. Local and Global variables
# 4. File handling.
# 5. Built in Python libraries
# 6. if __name__ == "__main__"

# We make a python file

# try:
#     f = open("python", "w")
#     f.write("Python is an Interactive Language found in 1997." \
#     "Simple synthax easy to write and read a python code. ")
#     # print(f.read())
#     f.close()
# except FileNotFoundError:
#     print("File doesn't exist...")

# f.write("Python developed by Gaudio Van rassam in 1991.")


# import pickle

# def main():

#     f = open("file1", "w")
#     pickle.dump(["hello", "world"], f)
#     pickle.dump({1:"one",2:"Two"}, f)
#     f.close()

#     f = open("file1","r")
#     value1 = pickle.load(f)
#     value2 = pickle.load(f)
#     print(value1, value2)
#     f.close()

# if __name__ == '__main__':
#     main()


# Types of errors in python
# 1.  Synthax Error.
# print("Hello)

"""
  File "d:\Generative-AI-Engineering\Python_for_GenAI\week_03\class_01\practice.py", line 44
    print("Hello)
          ^
SyntaxError: unterminated string literal (detected at line 44)

"""
# for i in range(0, 10)

# 2. Indentation Error:
# marks =  Input ("Enter your marks:....")

"""
 File "d:\Generative-AI-Engineering\Python_for_GenAI\week_03\class_01\practice.py", line 56, in <module>
    marks =  Input ("Enter your marks:....")
             ^^^^^
NameError: name 'Input' is not defined. Did you mean: 'input'?

"""
# 3. Type Error..

# sumtwonum = "Sum of 2 and 5 " + 5
# print(sumtwonum)

"""
 File "d:\Generative-AI-Engineering\Python_for_GenAI\week_03\class_01\practice.py", line 67, in <module>
    sumtwonum = "Sum of 2 and 5 " + 5
                ~~~~~~~~~~~~~~~~~~^~~
TypeError: can only concatenate str (not "int") to str

"""

# 4. ValueError

# num1 = int("Hello")
# print(num1)

"""
 File "d:\Generative-AI-Engineering\Python_for_GenAI\week_03\class_01\practice.py", line 80, in <module>
    num1 = int("Hello")
ValueError: invalid literal for int() with base 10: 'Hello'

"""
# 5. ZeroDivisionError

# num1 = 10
# num2 = 0

# divide = num1/num2
# print(divide)
"""
 File "d:\Generative-AI-Engineering\Python_for_GenAI\week_03\class_01\practice.py", line 94, in <module>
    divide = num1/num2
             ~~~~^~~~~
ZeroDivisionError: division by zero
"""

# 6. OSError

# f = open("GenAI_data2.txt", "r")
"""
 File "d:\Generative-AI-Engineering\Python_for_GenAI\week_03\class_01\practice.py", line 105, in <module>
    f = open("GenAI_data2.txt", "r")
FileNotFoundError: [Errno 2] No such file or directory: 'GenAI_data2.txt'

"""

# 7. IndexError

# color = ["red","green", "blue"]
# print(color[4])

"""
  File "d:\Generative-AI-Engineering\Python_for_GenAI\week_03\class_01\practice.py", line 116, in <module>
    print(color[4])
          ~~~~~^^^
IndexError: list index out of range

"""

# try and Exception
# import sys

# def main():
#     """
#     Objective: to Open a File to reading
#     input parameter: None
#     Return Value: None

#     """

#     try:
#         f = open("temporary_file","r")

#     except IOError as err:
#         print("Problem with input output...\n", err)
#         print(sys.exc_info())

#     print("Program continus beyond try ...except block")

# if __name__ == "__main__":
#     main()

# Example
import sys
def main():
    """
    Objective: To Compute Price Per unit weight of item
    input Parameter : None
    return Value: None
    
    """
    price = input('Enter a Price of Item Purchased: ')
    weight = input('Enter a weight of Item Purchased: ')

    try:
        if price =='': price = None
        price = float(price)

        if weight =='': weight = None
        weight = float(weight)

        price >= 0 and weight >= 0
        result = price / weight

    except (ValueError, TypeError, ZeroDivisionError):
        print('Invalid Input provider by user \n' +  str(sys.exc_info()))

    else:
        print('Price Per unit weight: ', round(result),2)

if __name__ == "__main__":
    main()



# 1. Create a file and write student information

with open("students.txt", "w") as file:
    file.write("Muhammad Irfan, Data Science, 85\n")
    file.write("Ali, Computer Science, 78\n")
    file.write("Ahmed, Software Engineering, 91\n")


# 2. Read the file

with open("students.txt", "r") as file:
    data = file.read()

print("Student Records:")
print(data)


# 3. Add a new student

with open("students.txt", "a") as file:
    file.write("Hassan, Artificial Intelligence, 88\n")


# 4. Read the updated file line by line

print("Updated Student Records:")

with open("students.txt", "r") as file:
    for line in file:
        print(line.strip())

# Add tasks to file

task = input("Enter a task: ")

with open("tasks.txt", "a") as file:
    file.write(task + "\n")

print("Task added successfully!")


# Display all tasks

print("\nYour Tasks:")

with open("tasks.txt", "r") as file:
    for number, task in enumerate(file, start=1):
        print(f"{number}. {task.strip()}")