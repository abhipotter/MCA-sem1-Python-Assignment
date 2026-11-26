a = list(map(int,input('Enter numbers: ').split()))
a = sorted(set(a))
if len(a) < 2:
    print('No second largest')
else:
    print('Second largest:',a[-2])
