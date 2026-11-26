def power(a,n):
    if n == 0:
        return 1
    if n < 0:
        return 1/power(a,-n)
    return a*power(a,n-1)

a = float(input('Base: '))
n = int(input('Power: '))
if a == 0 and n < 0:
    print('Undefined')
else:
    print(power(a,n))
