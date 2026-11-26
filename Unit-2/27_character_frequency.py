s = input('Enter string: ')
f = {}
for ch in s:
    f[ch] = f.get(ch,0)+1
print(f)
