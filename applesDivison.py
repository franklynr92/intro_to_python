print("We have 10 pounds of Apples.")
number = input("How many ways are we dividing the apples?")
number = int(number)
try:
    poundsEach = 10/number
    print("Each person gets", poundsEach, "pounds of apples.")
except ZeroDivisionError:
    print("You can't divide by zero. Try again")
