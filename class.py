from unicodedata import name

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def myfunc(self):
        print("Hello my name is " + self.name)
        print("My age is " + self.age)
        print("I am in " + self.grade + " grade")

p1 = Student("Amaryllis", "fifteen", "tenth")
#p2 = Student("Benedict", "twenty five", "twelfth")
#p3 = Student("Sophie", "fifteen", "tenth")

p1.myfunc()
#p2.myfunc()
#p3.myfunc()

class Courses:
    def __init__(self, name):
        self.course = name

    def myfunc(self):
        print("I am in " + self.course + " class")

p1 = Courses("History")

p1.myfunc()



