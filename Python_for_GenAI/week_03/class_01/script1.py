# Exceptions

# try:
#     num = int(input("Enter a number: "))
#     print(num)
# except ValueError:
#     print("Invalid input. Please enter a valid integer.")

# example of raising a custom exception
# try:
#     num = int(input("Enter a number: "))
#     divisor = int(input("Enter a divisor: "))
#     if divisor == 0:
#         raise ZeroDivisionError("Divisor cannot be zero.")
#     result = num / divisor
#     print(f"Result: {result}")
# except ValueError:
#     print("Invalid input. Please enter a valid integer.")

# Example 2: try, except, else, finally

# try:
#     num = int(input("Enter a number: "))
#     divisor = int(input("Enter a divisor: "))
#     if divisor == 0:
#         raise ZeroDivisionError("Divisor cannot be zero.")
#     result = num / divisor
# except ValueError:
#     print("Invalid input. Please enter a valid integer.")
# except ZeroDivisionError as e:
#     print(f"Error: {e}")
# else:
#     print(f"Result: {result}")
# finally:
#     print("Execution completed.")

# # Example 3: Custom Exception Class


# class InsufficientFundsError(Exception):
#         """Custom exception for insufficient funds."""
#         pass
# try:
#     balance = float(input("Enter your account balance: "))
#     withdrawal_amount = float(input("Enter the amount to withdraw: "))

#     if balance < withdrawal_amount:
#             raise InsufficientFundsError("Insufficient funds for the withdrawal.")
#     balance -= withdrawal_amount
#     print(f"Withdrawal successful. New balance: {balance}")
# except ValueError:
#     print("Invalid input. Please enter a valid number.")
# except InsufficientFundsError as e:
#     print(f"Error: {e}")



# Local and Global Variables

# name = " Muhammad Ali"  # Global variable

# def ChangeName():
#     global name  # Declare 'name' as a global variable
#     name = "Muhammad Ali Jinnah"  # Modify the global variable
#     print("Inside function:", name)

# ChangeName()
# print("Outside function:", name)

# File Handling 

"""
open() function is used to open a file in Python. 
It takes two parameters: the file name and the mode in which the file should be opened.
"r" - Read mode (default): Opens a file for reading. The file pointer is placed at the beginning of the file. If the file does not exist, it raises a FileNotFoundError.
"w" - Write mode: Opens a file for writing. If the file already exists,
"a" - Append mode: Opens a file for appending. If the file already exists, the file pointer is placed at the end of the file. If the file does not exist, it creates a new file.

# """
    
# with open("GenAI_Data.txt", "w") as f:
#     f.write("This is a sample text written to the file.\n")
#     f.write("You can write multiple lines to the file.\n")
#     f.write("File handling in Python is straightforward.\n")

# with open("GenAI_Data.txt", "r") as f:
#     content = f.read()

# try:
#     with open("GenAI_Data.txt", "r") as f:
#         content = f.read()
#         print(content)
# except FileNotFoundError:
#     print("File not found.")

# with open("GenAI_Data.txt", "w") as f:
#     f.write("This is a sample GenAI text.\n")
#     f.write("You can write data to the file.\n")
#     f.write("File handling in Python.\n")


# # Built in Python Libraries
# import math
# print(math.sqrt(25))

# from pathlib import Path

# path = Path("D:\\Generative-AI-Engineering\\GenAI_Data.txt")
# print(path.exists())

# import random

# num = random.randint(2,10)
# print (num)

# import datetime

# import datetime

# current_time = datetime.datetime.now().time()
# print(current_time)



# If __name__ == "__main__"
""""
block of code runs only when the Python file is executed directly, 
not when it is imported as a module.

"""
def myName():
    print("My name is Jack.")


def age():
    print("I am 17 years old.")


def city():
    print("I'm from Malta.")


def main():
    myName()
    age()
    city()


if __name__ == "__main__":
    main()


from datetime import date

today = date.today()

expense = input("Enter expense: ")
amount = float(input("Enter amount: "))

with open("expenses.txt", "a") as file:
    file.write(f"{today} | {expense} | {amount}\n")

print("Expense saved successfully!")


print("\nExpense History:")

with open("expenses.txt", "r") as file:
    for line in file:
        print(line.strip())
