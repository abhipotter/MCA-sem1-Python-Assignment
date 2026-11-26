import copy
a = [[1,2],[3,4]]
b = copy.copy(a)
c = copy.deepcopy(a)
a[0][0] = 99
print('Original:',a)
print('Shallow copy:',b)
print('Deep copy:',c)
