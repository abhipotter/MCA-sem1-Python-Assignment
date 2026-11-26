from pathlib import Path
p = Path(__file__).with_name('sample.txt')
with open(p,'r',encoding='utf-8') as f:
    n = 0
    for line in f:
        n += 1
print('Lines:',n)
