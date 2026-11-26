a = float(input('First side: '))
b = float(input('Second side: '))
c = float(input('Third side: '))
if a > 0 and b > 0 and c > 0 and a+b > c and a+c > b and b+c > a:
    print('Valid triangle')
else:
    print('Invalid triangle')
