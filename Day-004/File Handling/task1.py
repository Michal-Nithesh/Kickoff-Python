# Open the file in write mode and write to it
file = open("/home/michalnithesh/Personal/Kickoff Python/Day-004/day4.txt", "w")
file.write("Today I have learned about File Handling")
file.close()

# # Open the file in read mode and read its content
# file = open("/home/michalnithesh/Personal/Kickoff Python/Day-004/day4.txt", "r")
# reading = file.read()
# print(reading)
# file.close()


# Open the file in append mode and append its content
file = open("/home/michalnithesh/Personal/Kickoff Python/Day-004/day4.txt", "a")
file.write("\nNow I am going to append a new line")
file.close()

# Open the file in read mode and read its content
file = open("/home/michalnithesh/Personal/Kickoff Python/Day-004/day4.txt", "r")
reading = file.read()
print(reading)
file.close()