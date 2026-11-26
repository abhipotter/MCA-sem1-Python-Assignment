from pathlib import Path
p = Path(__file__).with_name('append.txt')
if not p.exists():
    p.write_text('First line\n',encoding='utf-8')
s = input('Enter text: ')
with open(p,'a',encoding='utf-8') as f:
    f.write(s+'\n')
with open(p,'r',encoding='utf-8') as f:
    print(f.read())
