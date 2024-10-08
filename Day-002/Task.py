def print_table(num):
    for i in range(1, 11):
        print(i, "x", num, "=", num * i)


number = int(input("Enter a number: "))


print_table(number)