s = input('Enter string: ').lower()
letters = 'abcdefghijklmnopqrstuvwxyz'
if all(ch in s for ch in letters):
    print('Pangram')
else:
    print('Not a pangram')
