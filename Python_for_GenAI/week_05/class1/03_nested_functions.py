# ------------------------------------------------------------
# Nested Function
# Use case: Helper logic ko outer function ke andar rakhna ho
# taake wo sirf usi function ke context mein use ho.
# ------------------------------------------------------------

# def outer_function():
#     print("Outer function started")

#     def inner_function():
#         print("Inner function executed")

#         def inner_function2():
#             print("Inner function2 executed")
#         inner_function2()
#     inner_function()


# outer_function()


# # ------------------------------------------------------------
# # Access Outer Function Variable
# # Use case: Inner function outer function ke local variables ko
# # directly use kar sakta hai without passing them again.
# # ------------------------------------------------------------

# def outer_function():
#     message = "Machine Learning"

#     def inner_function():
#         print(message)

#     inner_function()


# outer_function()

# # ------------------------------------------------------------
# # Nested Function in an ML-Style Workflow
# # Use case: Main preprocessing function ke andar helper function
# # ko define karke individual values ko normalize karna.
# # ------------------------------------------------------------

# # def preprocess_data(data):
# #     max_value = max(data)

# #     def normalize(value):
# #         return value / max_value

# #     processed_data = [normalize(x) for x in data]

# #     return processed_data


# # data = [10, 20, 30, 40]

# # result = preprocess_data(data)

# # print(result)



# # ------------------------------------------------------------
# # ------------------------------------------------------------
# # Example 1: Default Parameters in Machine Learning
# # Use case: Model training ke liye commonly used settings ko
# # default values dena, taake har call par repeat na karna pade.
# #
# # Parameters:
# # model_name -> required parameter
# # epochs -> default parameter
# # batch_size -> default parameter
# #
# # Arguments:
# # "CNN" -> positional argument
# # epochs=25 -> keyword argument
# # batch_size=64 -> keyword argument
# # ------------------------------------------------------------

# def train_model(model_name, epochs=10, batch_size=32):
#     print("Model:", model_name)
#     print("Epochs:", epochs)
#     print("Batch Size:", batch_size)


# train_model("CNN")
# train_model("CNN", epochs=25, batch_size=64)

# # ------------------------------------------------------------
# # ------------------------------------------------------------
# # **kwargs for Neural Network Configuration
# # Use case: Model ki optional settings ko flexible way mein
# # function ko pass karna.
# #
# # **settings:
# # Har argument name=value form mein diya jata hai.
# # Ye dictionary ki form mein function ke andar available hota hai.
# # ------------------------------------------------------------

# def build_model(**settings):

#     print("Optimizer:", settings["optimizer"])
#     print("Learning Rate:", settings["learning_rate"])
#     print("Activation:", settings["activation"])


# build_model(
#     optimizer="Adam",
#     learning_rate=0.001,
#     activation="relu")


# def add_item(name, employee_data=[]):
#     employee_data.append(name)
#     print("update data is ", employee_data)

# add_item("Kamran")
# print(add_item.__defaults__)
# add_item("Aslam")
# print(add_item.__defaults__)
# add_item("Ali")
# print(add_item.__defaults__)
# add_item("Lala")
# print(add_item.__defaults__)



