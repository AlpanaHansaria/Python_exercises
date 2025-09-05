"""
23.	Student Marks Management
o	Store students with marks.
o	Calculate total, average, grade using OOP.
"""

class Student:
    def __init__(self, name, english, maths, biology, history, spanish):
        self.name = name
        self.english = english
        self.maths = maths
        self.biology = biology
        self.history = history
        self.spanish = spanish

    def total_marks(self):
        self.total = self.english + self.maths + self.biology + self.history + self.spanish
        return self.total
    
    def average_marks(self):
        self.average = self.total/5
        return self.average
    
    def grade(self):
        if self.average >= 90:
            return "A\n"
        elif self.average >= 80:
            return "B\n"
        elif self.average >= 70:
            return "C\n"
        elif self.average >= 60:
            return "D\n"
        else:
            return "F\n"
        
# Run
Student1 = Student("Alice", 85, 92, 78, 88, 90)
print("Student 1: ", Student1.name)
print("Total Marks:", Student1.total_marks())
print("Average Marks:", Student1.average_marks())
print("Grade:", Student1.grade())

Student2 = Student("Bob", 75, 80, 70, 65, 90)
print("Student 2: ", Student2.name)
print("Total Marks:", Student2.total_marks())
print("Average Marks:", Student2.average_marks())
print("Grade:", Student2.grade())

Student3 = Student("Charlie", 95, 98, 92, 90, 94)
print("Student 3: ", Student3.name)
print("Total Marks:", Student3.total_marks())
print("Average Marks:", Student3.average_marks())
print("Grade:", Student3.grade())   

Student4 = Student("David", 55, 60, 58, 62, 70)
print("Student 4: ", Student4.name)
print("Total Marks:", Student4.total_marks())
print("Average Marks:", Student4.average_marks())
print("Grade:", Student4.grade())