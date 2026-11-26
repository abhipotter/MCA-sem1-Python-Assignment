from pathlib import Path
p = Path(__file__).with_name('sample.txt')
with open(p,'r',encoding='utf-8') as f:
    print(f.read())
