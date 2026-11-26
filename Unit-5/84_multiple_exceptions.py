try:
    a = int(input('First number: '))
    b = int(input('Second number: '))
    print(a/b)
except ValueError:
    print('Enter integers only')
except ZeroDivisionError:
    print('Division by zero')
