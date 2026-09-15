# Type Conversion

# costPrice = int(input("Enter the cost price: "))
# profit = int(input("Enter the profit: "))
# sellingPrice = costPrice + profit
# print ("The selling price is:", sellingPrice)

# Random fucntion

# import random
# # Generate a random number between 1 and 10

# if random.random() < 0.5:
#     print("Player A will be the player first.")
# else:
#       print("Player B will be the player first.")


# Math fucntion

# import math

# num1 =  39.5
# print(math.ceil(num1))

# print(math.floor(num1))

# print(math.sqrt(num1))

# print(math.pow(num1, 2))

# print(math.factorial(5))

# print(math.gcd(12, 18))

# print(math.lcm(12, 18))

# print(math.fabs(-39.5))

# print(math.degrees(num1))


# import math


# dir (__builtins__)

# help(math.cos)



# print a triangle pattern using nested loops
# def main():
#     print("*")
#     print("**")
#     print("***")
#     print("****")
#     print("*****")

#     # space

#     print ()

#     # Print a Square pattern

#     print("****")
#     print("****")
#     print("****")
#     print("****")


# def triangle():

#     # Print a triangle 
#     print("   *")
#     print("  ** ")
#     print(" ***")
#     print("****")
#     print("*****")
    

#     print()

# def square():
#     # Print a square pattern
#     print("* * * *")
#     print("* * * *")
#     print("* * * *")
#     print("* * * *")

# def main():
#     triangle()

#     print() # space

#     square()    

# if __name__ == "__main__":
#     main()
# print("End of the program.")


# # print triangle
# def triangle():
#     print(" *")
#     print("***")
#     print("*****")
#     print("*******")

# def main():
#     triangle()

# if __name__ == "__main__":
#     main()


# Area of rectangle
def areaRectangle(length, width):
    area = length * width
    return area

def main():
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    areaRect = areaRectangle(length, width)
    print("The area of the rectangle is:", areaRect)

if __name__ == "__main__":
    main()
print("End of the program.")