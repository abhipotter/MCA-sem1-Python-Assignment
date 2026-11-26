def gcd(a,b):
    a,b = abs(a),abs(b)
    while b != 0:
        a,b = b,a%b
    return a

a = int(input('First number: '))
b = int(input('Second number: '))
print('GCD:',gcd(a,b))
