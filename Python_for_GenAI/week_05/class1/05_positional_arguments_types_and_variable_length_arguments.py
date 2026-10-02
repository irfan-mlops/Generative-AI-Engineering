# ============================================================
# 05 - Positional Arguments, Argument Types & Variable Arguments
# ============================================================


# ------------------------------------------------------------
# 1. Positional Arguments
# ------------------------------------------------------------

def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")


introduce("Irfan", 25)

# Arguments are matched according to their position:
# name = "Irfan"
# age = 25


# ------------------------------------------------------------
# 2. Keyword Arguments
# ------------------------------------------------------------

introduce(age=25, name="Irfan")

# Keyword arguments are matched using parameter names,
# so their order does not matter.


# ------------------------------------------------------------
# 3. Different Argument Types
# ------------------------------------------------------------

def student_info(name, age, university):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"University: {university}")


student_info(
    "Irfan",
    25,
    "Dong-A University"
)


# ------------------------------------------------------------
# 4. *args - Variable-Length Positional Arguments
# ------------------------------------------------------------

def calculate_sum(*numbers):
    total = 0

    for number in numbers:
        total += number

    return total


print(calculate_sum(10, 20))
print(calculate_sum(10, 20, 30, 40))
print(calculate_sum(1, 2, 3, 4, 5))


# *args stores multiple positional arguments in a tuple.


# ------------------------------------------------------------
# 5. **kwargs - Variable-Length Keyword Arguments
# ------------------------------------------------------------

def show_profile(**information):
    for key, value in information.items():
        print(f"{key}: {value}")


show_profile(
    name="Irfan",
    field="Data Science",
    university="Dong-A University"
)


# **kwargs stores multiple keyword arguments in a dictionary.


# ------------------------------------------------------------
# 6. Combining Normal Arguments, *args and **kwargs
# ------------------------------------------------------------

def profile(name, *skills, **details):
    print(f"Name: {name}")

    print("Skills:")
    for skill in skills:
        print(f"- {skill}")

    print("Details:")
    for key, value in details.items():
        print(f"- {key}: {value}")


profile(
    "Irfan",
    "Python",
    "RAG",
    "LLMs",
    university="Dong-A University",
    role="AI Researcher"
)


# ------------------------------------------------------------
# Important Rule
# ------------------------------------------------------------

# The order of parameters should be:
#
# normal parameters
#       ↓
# *args
#       ↓
# **kwargs
#
# Example:
#
# def function(name, *args, **kwargs):
#     pass

