c = input('Enter character: ')
if len(c) != 1:
    print('Enter only one character')
elif c.isalpha():
    print('Alphabet')
elif c.isdigit():
    print('Digit')
else:
    print('Special character')
