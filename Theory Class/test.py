class Student:
    def __init__(self,name):
        self.name = name
        self.age = 18

    def show_name(self):
        print(self.name)
        print(self.age)

user = input("Enter the Name: ")
student1 = Student(user)

student1.show_name()
