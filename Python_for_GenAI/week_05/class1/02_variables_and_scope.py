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

# ------------------------------------------------------------
# Resolve UnboundLocalError Using the global Keyword
# Use case: Use this approach when a function needs to modify
# a variable that was originally created outside the function.
# ------------------------------------------------------------

# num = 10  # Global variable


# def display():
#     global num  # Tells Python to use the global 'num' variable
#     num += 10   # Updates the global variable
#     print("Inside:", num)
#     return num

# display()
# print("Outside:", num)

# #====================================================================================

# # ------------------------------------------------------------
# # Multiple Return Statements
# # Use case: Return different results based on different
# # conditions.
# # ------------------------------------------------------------

# def check_number(num):
#     if num > 0:
#         return "Positive"

#     if num < 0:
#         return "Negative"

#     return "Zero"


# print(check_number(10))
# print(check_number(-5))
# print(check_number(0))

# # ------------------------------------------------------------
# # Normalize Input Data
# # Use case: ML model ko data dene se pehle values ko 0-1 range
# # mein scale karta hai aur processed data ko return karta hai.
# # ------------------------------------------------------------

# def normalize_data(data):
#     min_value = min(data)
#     max_value = max(data)

#     normalized_data = [
#         (x - min_value) / (max_value - min_value)
#         for x in data]

#     return normalized_data


# data = [10, 20, 30, 40, 50]

# processed_data = normalize_data(data)

# print("Original Data:", data)
# print("Normalized Data:", processed_data)


# # ------------------------------------------------------------
# # Make Prediction
# # Use case: Trained ML model ko input data deta hai aur model ki
# # predicted output ko return karta hai.
# # ------------------------------------------------------------

# def make_prediction(model, input_data):
#     prediction = model.predict(input_data)
#     return prediction

# # ------------------------------------------------------------
# # Calculate Accuracy
# # Use case: Actual aur predicted labels compare karke model ki
# # accuracy calculate karta hai aur result return karta hai.
# # ------------------------------------------------------------

# from sklearn.metrics import accuracy_score


# def evaluate_model(y_true, y_pred):
#     accuracy = accuracy_score(y_true, y_pred)
#     return accuracy


# accuracy = evaluate_model(y_test, y_pred)

# print("Model Accuracy:", accuracy)


# ------------------------------------------------------------
# Train ML Model
# Use case: Model ko training data par train karta hai, test data
# par predictions banata hai, aur trained model + predictions
# dono return karta hai for later evaluation or deployment.
# ------------------------------------------------------------

# from sklearn.linear_model import LogisticRegression


# def train_model(X_train, y_train, X_test):
#     model = LogisticRegression()

#     model.fit(X_train, y_train)

#     predictions = model.predict(X_test)

#     return model, predictions



# ------------------------------------------------------------
# Function as an Object
# Use case: Python functions can be stored in variables just
# like numbers, strings, lists, or other objects.
# ------------------------------------------------------------

def greet():
    return "Hello"


print(greet)        # Shows the function object
print(type(greet))  # Shows its type

# ------------------------------------------------------------
# Function Alias
# Use case: Create another name for the same function without
# creating a new function.
# ------------------------------------------------------------

def greet():
    return "Hello"


say_hello = greet  # Function alias

print(greet())
print(say_hello())


# ------------------------------------------------------------
# Function Reference vs Function Call
# Use case: Understand the difference between storing a function
# and storing the result returned by that function.
# ------------------------------------------------------------

def greet():
    return "Hello"


alias = greet        # Stores function object
result = greet()     # Stores returned value

print(alias)
print(result)

# ------------------------------------------------------------
# Function Alias in ML-Style Workflow
# Use case: Assign a preprocessing function to another variable
# so it can be selected or reused dynamically.
# ------------------------------------------------------------

def normalize(data):
    return [x / max(data) for x in data]


preprocess = normalize  # Alias of normalize()

data = [10, 20, 30, 40]

processed_data = preprocess(data)

print(processed_data)

