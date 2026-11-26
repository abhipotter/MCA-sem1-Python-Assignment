def fact(n):
    if n <= 1:
        return 1
    return n*fact(n-1)

n = int(input('Enter number: '))
if n < 0:
    print('Invalid number')
else:
    print(fact(n))
