from itertools import permutations
s = input('Enter string: ')
for p in sorted(set(permutations(s))):
    print(''.join(p))
