class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

students = [Student('Aman',80),Student('Ravi',75)]
students.append(Student('Neha',90))
students[0].marks = 85
students.pop(1)
for s in students:
    print(s.name,s.marks)
