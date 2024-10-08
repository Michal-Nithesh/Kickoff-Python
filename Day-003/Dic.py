person = {
    "name": "Michal",
    "age": "21",
    "stuYear": "3rd",
    "Course": "Computer Science"
}

print(person)

print(person["name"])

person["age"] = 20

person["professional"] = "Developer"

print(person)

for key, value in person.items():
    print(key, ":", value)