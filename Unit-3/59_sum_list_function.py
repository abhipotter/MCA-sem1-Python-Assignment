def total(a):
    s = 0
    for n in a:
        s += n
    return s

a = list(map(int,input('Enter numbers: ').split()))
print(total(a))
