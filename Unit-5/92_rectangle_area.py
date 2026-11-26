class Rectangle:
    def __init__(self,l,b):
        self.l = l
        self.b = b

    def area(self):
        return self.l*self.b

l = float(input('Length: '))
b = float(input('Breadth: '))
if l > 0 and b > 0:
    print('Area:',Rectangle(l,b).area())
else:
    print('Invalid dimensions')
