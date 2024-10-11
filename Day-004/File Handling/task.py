try:
    fileName = input("Enter the file name: ")
    file = open(fileName, "r")
    content = file.read()
except FileExistsError:
    print("file doesn't exist")