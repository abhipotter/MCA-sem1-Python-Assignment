s = input('Enter string: ').lower()
v,c = 0,0
for ch in s:
    if 'a' <= ch <= 'z':
        if ch in 'aeiou':
            v += 1
        else:
            c += 1
print('Vowels:', v)
print('Consonants:', c)
