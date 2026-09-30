# ============================================================
# Python Variables and Scope
# ============================================================
# This file covers identifiers, variables, and variable scope.
# ============================================================


# ------------------------------------------------------------
# 1. Identifier
# ------------------------------------------------------------

# An identifier is the name given to a variable, function,
# class, or other object in Python.

name = "Kim"
age = 25
course = "Data Science"
# ------------------------------------------------------------
# 2. Variable
# ------------------------------------------------------------

# A variable is a name that refers to a value.
# Here, 'name' refers to the string value "Kim".

name = "Kim"

# Here, 'age' refers to the integer value 25.
age = 25

print(name)
print(age)

# ------------------------------------------------------------
# 3. Local Variable
# ------------------------------------------------------------

# A local variable is created inside a function.
# It can normally be used only inside that function.

def student_info(name):
    # 'age' is a local variable.
    age = 25
    print(name)
    print(age)
    print(locals())

student_info("kim")


# ------------------------------------------------------------
# 4. Global Variable
# ------------------------------------------------------------

# A global variable is created outside a function.
# It can be accessed from different parts of the program.

name = "Irfan"


# def display_name():
#     # Access the global variable inside the function.
#     print(name)
#     print(globals())

# display_name()

# How to resolve unBoundlocalerror
num = 10 # Global Variable
def display():
    global num
    num =  num + 10 # local Variable
    print("Inside", num)

display()
print("outside",num)