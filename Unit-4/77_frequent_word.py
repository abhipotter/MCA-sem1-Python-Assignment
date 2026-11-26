from pathlib import Path
import re
p = Path(__file__).with_name('sample.txt')
with open(p,'r',encoding='utf-8') as f:
    words = re.findall(r'\w+',f.read().lower())
d = {}
for word in words:
    d[word] = d.get(word,0)+1
if d:
    w = max(d,key=d.get)
    print(w,d[w])
else:
    print('Empty file')
