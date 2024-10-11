class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course
        
    def display_info(self):
        print(f"Student: {self.name}, Age: {self.age}, Course: {self.course}")
        
student_1 = Student("Michal", 21, "Computer Science")
student_1.display_info() 

student_2 = Student("Alice", 22, "Mechanical Engineering")
student_2.display_info()
