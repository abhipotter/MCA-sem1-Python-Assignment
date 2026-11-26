from pathlib import Path
p = Path(__file__).with_name('numbers.txt')
a = [10,20,30,40,50]
with open(p,'w',encoding='utf-8') as f:
    for n in a:
        f.write(str(n)+'\n')
print('Numbers saved')
