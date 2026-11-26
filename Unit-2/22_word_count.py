s = input('Enter sentence: ').lower().split()
for word in dict.fromkeys(s):
    print(word, s.count(word))
