n = int(input('Enter number: '))
s = str(n)
if s == s[::-1]:
    print('Palindrome')
else:
    print('Not a palindrome')
