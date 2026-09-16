# Area of rectangle
def areaRectangle(length, width):
    area = length * width
    return area

def areaSquare(side):
    area = side * side
    return area

def main():
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    areaRect = areaRectangle(length, width)
    print("The area of the rectangle is:", areaRect)

    side = float(input("Enter the side of the square: "))
    areaSquare = areaSquare(side)
    print("The area of the square is:", areaSquare)

if __name__ == "__main__":
    main()
# Display a message indicating the end of the program
print("End this program.")