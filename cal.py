print("\n****** AREA CALCULATOR ******")

while True:

    print("""
Press 1 to get the area of Square
Press 2 to get the area of Circle
Press 3 to get the area of Triangle 
Press 4 to get the area of Rectangle

""")

    choice = int(input("Enter a number between 1-4: "))

    if choice == 1:
        while True:
          side = float(input("Enter the side of square: "))
          area = side ** 2
          print("Area of Square =", area)
          repeat = input("Do you want to calculate again? (y/n): ")
          if repeat == "no" or repeat == "n":
            print("Thank you for using Area Calculator!")
            break

    elif choice == 2:
        while True:
          radius = float(input("Enter the radius of circle: "))
          area = (22/7) * radius ** 2
          print("Area of Circle =", area)
          repeat = input("Do you want to calculate again? (y/n): ")
          if repeat == "no" or repeat == "n":
            print("Thank you for using Area Calculator!")
            break

    elif choice == 3:
        while True:
          base = float(input("Enter the base of triangle: "))
          height = float(input("Enter the height of triangle: "))
          area = 0.5 * base * height
          print("Area of Triangle =", area)
          repeat = input("Do you want to calculate again? (y/n): ")
          if repeat == "no" or repeat == "n":
            print("Thank you for using Area Calculator!")
            break

    elif choice == 4:
        while True:
          length = float(input("Enter the length of rectangle: "))
          width = float(input("Enter the width of rectangle: "))
          area = length * width
          print("Area of Rectangle =", area)
          repeat = input("Do you want to calculate again? (y/n): ")
          if repeat == "no" or repeat == "n":
            print("Thank you for using Area Calculator!")
            break


repeat1 = input("Do you want to calculate again? (y/n): ")
if repeat1 == "no" or repeat1 == "n":
    print("Thank you for using Area Calculator!")
    exit()