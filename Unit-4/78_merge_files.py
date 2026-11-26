from pathlib import Path
p = Path(__file__).parent
with open(p/'merged.txt','w',encoding='utf-8') as out:
    for name in ['sample.txt','second.txt']:
        with open(p/name,'r',encoding='utf-8') as f:
            out.write(f.read().rstrip('\n')+'\n')
print('Files merged')
