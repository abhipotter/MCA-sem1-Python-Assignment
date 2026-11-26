a = list(map(int,input('Enter numbers: ').split()))
if a:
    print('Largest:', max(a))
    print('Smallest:', min(a))
else:
    print('Empty list')
