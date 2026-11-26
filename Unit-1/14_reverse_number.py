n = int(input('Enter number: '))
r = int(str(abs(n))[::-1])
if n < 0:
    r = -r
print('Reverse:', r)
