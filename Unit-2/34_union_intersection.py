a = list(map(int,input('First list: ').split()))
b = list(map(int,input('Second list: ').split()))
print('Union:', sorted(set(a)|set(b)))
print('Intersection:', sorted(set(a)&set(b)))
