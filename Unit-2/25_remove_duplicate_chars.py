s = input('Enter string: ')
ans = ''
for ch in s:
    if ch not in ans:
        ans += ch
print(ans)
