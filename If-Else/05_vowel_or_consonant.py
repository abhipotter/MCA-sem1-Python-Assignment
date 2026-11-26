c = input('Enter alphabet: ').lower()
if len(c) != 1 or not ('a' <= c <= 'z'):
    print('Invalid alphabet')
elif c in 'aeiou':
    print('Vowel')
else:
    print('Consonant')
