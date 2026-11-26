a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))
if a >= b:
    if a >= c:
        largest = a
    else:
        largest = c
else:
    if b >= c:
        largest = b
    else:
        largest = c
print('Largest:', largest)
