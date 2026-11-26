d = {'name':'Aman','age':21,'city':'Kota'}
k = input('Key to remove: ')
if k in d:
    del d[k]
else:
    print('Key not found')
print(d)
