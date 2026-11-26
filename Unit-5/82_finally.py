try:
    n = int(input('Enter number: '))
    print(10/n)
except (ValueError,ZeroDivisionError):
    print('Invalid input')
finally:
    print('Program finished')
