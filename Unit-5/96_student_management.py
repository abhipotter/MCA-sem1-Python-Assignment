class Student:
    def __init__(self,roll,name,marks):
        self.roll = roll
        self.name = name
        self.marks = marks

class Management:
    def __init__(self):
        self.students = []

    def search(self,roll):
        for s in self.students:
            if s.roll == roll:
                return s

    def add(self,roll,name,marks):
        if self.search(roll):
            print('Roll number already exists')
        else:
            self.students.append(Student(roll,name,marks))
            print('Student added')

    def show(self):
        for s in self.students:
            print(s.roll,s.name,s.marks)
        if not self.students:
            print('No students')

    def delete(self,roll):
        s = self.search(roll)
        if s:
            self.students.remove(s)
            print('Student deleted')
        else:
            print('Student not found')

m = Management()
while True:
    print('1. Add  2. Show  3. Search  4. Update marks  5. Delete  6. Exit')
    ch = input('Choice: ')
    if ch == '1':
        roll = input('Roll number: ')
        name = input('Name: ')
        marks = float(input('Marks: '))
        if 0 <= marks <= 100:
            m.add(roll,name,marks)
        else:
            print('Invalid marks')
    elif ch == '2':
        m.show()
    elif ch == '3':
        s = m.search(input('Roll number: '))
        if s:
            print(s.roll,s.name,s.marks)
        else:
            print('Student not found')
    elif ch == '4':
        s = m.search(input('Roll number: '))
        if s:
            marks = float(input('New marks: '))
            if 0 <= marks <= 100:
                s.marks = marks
                print('Updated')
            else:
                print('Invalid marks')
        else:
            print('Student not found')
    elif ch == '5':
        m.delete(input('Roll number: '))
    elif ch == '6':
        break
    else:
        print('Invalid choice')
