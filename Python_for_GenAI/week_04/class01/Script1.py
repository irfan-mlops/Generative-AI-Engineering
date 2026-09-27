# Topics
# 01. Introduction of OPP
# 02. Class and Objects
# 03. Attributes and Methods 
# 04. Constructor
# 05. Magic and (Dhunder) methods
# 06. Encapsulations
# 07. Static Methods
# 08. Inheritance 
# 09. Types of Inheritance

# class Student:
#     # magic/dunder methods > Constructor
#     def __init__(self, arg_name, arg_age, arg_course):
#         self.name = arg_name
#         self.age = arg_age
#         self.course = arg_course

#     def introduce(self):
#         print(f"I am {self.name} and i am Learning OOP to Become a  Good Programmer.")

#     def __str__(self):
#         return f"Student : {self.name} | {self.age} | {self.course}"

#     def __len__(self):
#         return len(self.name)
    
# student1 = Student("Kaleem", 35, "GenAi")

# student1.introduce()
# print(student1)
# print(f"The length of {len(student1)}")


# #=============================================================
# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.__balance =  balance

    
#     def show_balance(self): # Getter To Read a Private Variable
#         print(f"The Balance is Rs.{self.__balance}")

#     def __str__(self):
#         return f"The bank Balance of  {self.owner} is | {self.balance}."


# account1 = BankAccount("Kaleem", 50000)
# # account1.show_balance()

# print(account1.owner)
# print(account1._BankAccount__balance) # Name Mangling


# Static Method

# class Mathhelper:

#     @staticmethod
#     def add(a, b):
#         return a + b
    
#     @staticmethod
#     def multiply(a,b):
#         return a * b

# prob1 = Mathhelper()
# print(prob1.add(30,20))

    
#=======================================
# Inheritance

# class Animal:
#     def eat(self):
#         print("Animal is eating..")
# class Dog(Animal):
#     def bark(self):
#         print("Dog is Barking..")

# jenny = Animal()
# jenny = Dog()
# jenny.bark()
# jenny.eat()



class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self,name, course):
        super().__init__(name)
        self.course = course

    def describe_course(self):
        print(f"My name is {self.name} and i have this {self.course} course.")

student1 = Student("Hamza", "genAi")
student1.describe_course()