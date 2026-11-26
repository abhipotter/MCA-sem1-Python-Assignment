t = (10,20,30,40)
n = int(input('Enter number: '))
if n in t:
    print('Index:',t.index(n))
else:
    print('Not found')
