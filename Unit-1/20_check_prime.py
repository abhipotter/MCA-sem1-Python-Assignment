n = int(input('Enter number: '))
prime = n >= 2
for i in range(2,int(max(n,0)**0.5)+1):
    if n%i == 0:
        prime = False
        break
if prime:
    print('Prime')
else:
    print('Not prime')
