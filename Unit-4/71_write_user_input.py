from pathlib import Path
p = Path(__file__).with_name('user_text.txt')
s = input('Enter text: ')
with open(p,'w',encoding='utf-8') as f:
    f.write(s)
print('File created')
