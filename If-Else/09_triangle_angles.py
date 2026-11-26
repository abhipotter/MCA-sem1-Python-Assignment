a = int(input('First angle: '))
b = int(input('Second angle: '))
c = int(input('Third angle: '))
if a > 0 and b > 0 and c > 0 and a+b+c == 180:
    print('Valid triangle')
else:
    print('Invalid triangle')
