import math
r = float(input('Radius: '))
if r < 0:
    print('Invalid radius')
else:
    print('Area:',round(math.pi*r*r,2))
