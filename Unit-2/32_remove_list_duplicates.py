a = list(map(int,input('Enter numbers: ').split()))
b = []
for n in a:
    if n not in b:
        b.append(n)
print(b)
