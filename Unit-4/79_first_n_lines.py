from pathlib import Path
p = Path(__file__).with_name('sample.txt')
n = int(input('Number of lines: '))
with open(p,'r',encoding='utf-8') as f:
    for i in range(max(0,n)):
        line = f.readline()
        if line == '':
            break
        print(line.rstrip())
