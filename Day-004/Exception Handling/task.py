try:
    number1 = int(input("Enter the First Number:"))
    number2 = int(input("Enter the Second Number:"))
    div = number1 / number2
    print("The divisible of two number is: ", div)
except ZeroDivisionError:
    print("Invalid input, Please enter a valid input")
finally:
    exit()