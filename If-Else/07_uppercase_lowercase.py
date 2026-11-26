c = input('Enter alphabet: ')
if len(c) != 1 or not c.isalpha():
    print('Invalid alphabet')
elif c.isupper():
    print('Uppercase')
elif c.islower():
    print('Lowercase')
else:
    print('No uppercase or lowercase form')
