# Data structures in Python
# List, Tuple, Set, Dictionary

# Lists are mutable, meaning their elements can be changed after creation.
# function in list: append(), extend(), remove(), pop(), sort(), reverse(), insert(), index(), count(), clear(), copy()
# list1 = [1, 2, 3, 4, 5, "Hello", True, 3.14]
# print("List:", list1)
# print("List[0]:", list1[0]) # Accessing first element
# print("List[-1]:", list1[-8]) # Accessing last element
# # Modifying list
# list1[0] = "Modified index 0 value"
# print("Modified List:", list1)
# list1.append("New Element") # Adding an element to the list
# print("List after appending:", list1)

# # extending list
# list1.extend([100, 200, 300]) # Adding multiple elements to the list
# print("List after extending:", list1)

# # Removing elements from the list
# list1.remove("Hello") # Removing an element from the list
# print("List after removing 'Hello':", list1)

# # Popping elements from the list
# popped_element = list1.pop() # Removing the last element from the list
# print("Popped Element:", popped_element)

# # Sorting the list
# list1.sort(key=str) # Sorting the list in ascending order
# print("Sorted List:", list1)

# # Reversing the list
# list1.reverse() # Reversing the list
# print("Reversed List:", list1)

# # Clearing the list
# list1.clear() # Removing all elements from the list
# print("Cleared List:", list1)

# # Slcing
# print("List[0:3]:", list1[0:3]) # Accessing first three elements

# Tuples are immutable, meaning their elements cannot be changed after creation.

# tuple1 = (1, 2, 3, 4, 5, "Hello", True, 3.14)
# print("Tuple:", tuple1)
# print("Tuple[0]:", tuple1[0]) # Accessing first element
# # Modifying tuple (not allowed)
# #  tuple1[0] = "Modified index 0 value" # This will raise an error
# print("Modified Tuple:", tuple1)

# # Membership testing
# print("Is 3 in tuple1?", 3 in tuple1) # Checking if an element is in the tuple

# # Counting elements in a tuple
# print("Count of 3 in tuple1:", tuple1.count(100)) # Counting occurrences of an element

# # Indexing elements in a tuple
# print("Index of 3 in tuple1:", tuple1.index(3)) # Finding the

# # Tuple Unqpacking using fucntion
# def unpack_tuple(name, age, city):
#     name  = input("Enter your name: ")
#     age = int(input("Enter your age: "))
#     city = input("Enter your city: ")

#     return (name, age, city)

# your_name, your_age, your_city = unpack_tuple("John", 25, "New York")
# print("Your Name:", your_name)
# print("Your Age:", your_age)
# print("Your City:", your_city)

# dictionaries are mutable, meaning their elements can be changed after creation.
# function in dictionary: keys(), values(), items(), get(), update(), pop(), popitem
# my_dict = { "age": 25, "city": "New York"}
# print("Dictionary:", my_dict)
# # print("Dictionary['name']:", my_dict["name"]) # Accessing value by key

# # Modifying dictionary
# my_dict["age"] = 26 # Changing the value of an existing key
# print("Modified Dictionary:", my_dict)

# # Adding a new key-value pair to the dictionary
# my_dict["country"] = "USA" # Adding a new key-value pair
# print("Dictionary after adding 'country':", my_dict)

# # Removing a key-value pair from the dictionary
# del my_dict["city"] # Removing a key-value pair
# print("Dictionary after removing 'city':", my_dict)

# # removing a key-value pair using pop()
# removed_value = my_dict.pop("age") # Removing a key-value pair using pop()
# print("Removed Value:", removed_value)
# print("Dictionary after popping 'age':", my_dict)

# # Get method to access value by key
# print("Get 'name':", my_dict.get("name")) # Accessing value by key using get()

# # Keys, Values, and Items methods
# print("Keys:", my_dict.keys()) # Getting all keys in the dictionary
# print("Values:", my_dict.values()) # Getting all values in the dictionary
# print("Items:", my_dict.items()) # Getting all key-value pairs in the dictionary

set1 = {1, 2, 3, 3 ,2, 44, 5}
print("Set:", set1) # unique values only

set1.add(100) # Adding an element to the set
print("Set after adding 100:", sorted(set1)) # Sorting the set

# Removing an element from the set
set1.remove(2) # Removing an element from the set
print("Set after removing 2:", sorted(set1)) # Sorting the set

# Membership testing
print("Is 3 in set1?", 3 in set1) # Checking if an element is in the set

# Intersection of two sets
set2 = {3, 4, 5, 6, 7}
intersection_set = set1.intersection(set2) # Finding the intersection of two sets
print("Intersection of set1 and set2:", sorted(intersection_set)) # Sorting the intersection set

# Union of two sets
union_set = set1.union(set2) # Finding the union of two sets
print("Union of set1 and set2:", sorted(union_set)) # Sorting the union set

# difference of two sets
difference_set = set1.difference(set2) # Finding the difference of two sets
print("Difference of set1 and set2:", sorted(difference_set)) # Sorting the difference

# Symmetric difference of two sets
symmetric_difference_set = set1.symmetric_difference(set2) # Finding the symmetric difference of two sets
print("Symmetric Difference of set1 and set2:", sorted(symmetric_difference_set)) # Sorting the symmetric difference set

# length of the set
print("Length of set1:", len(set1)) # Getting the length of the set

