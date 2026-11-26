class Student:
    course = 'MCA'

    @classmethod
    def change_course(cls,course):
        cls.course = course

    @staticmethod
    def is_pass(marks):
        return marks >= 40

Student.change_course('MCA 2026')
print(Student.course)
print('Passed:',Student.is_pass(75))
