class AgeError(Exception):
    pass

try:
    age = int(input('Enter age: '))
    if age < 18:
        raise AgeError('Age must be at least 18')
    print('Eligible')
except AgeError as e:
    print(e)
except ValueError:
    print('Invalid age')
