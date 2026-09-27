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

class Student:
    # magic/dunder methods > Constructor
    def __init__(self, arg_name, arg_age, arg_course):
        self.name = arg_name
        self.age = arg_age
        self.course = arg_course

    def introduce(self):
        print(f"I am {self.name} and i am Learning OOP to Become a  Good Programmer.")

    def __str__(self):
        return f"Student : {self.name} | {self.age} | {self.course}"

    def __len__(self):
        return len(self.name)
    
student1 = Student("Kaleem", 35, "GenAi")

student1.introduce()
print(student1)
print(f"The length of {len(student1)}")
