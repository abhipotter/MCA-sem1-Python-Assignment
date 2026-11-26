try:
    n = int(input('Enter number: '))
    print(100/n)
except ZeroDivisionError:
    print('Cannot divide by zero')
except ValueError:
    print('Invalid number')
