import os
from pathlib import Path
p = Path(__file__).parent
file = p/'os_demo.txt'
with open(file,'w',encoding='utf-8') as f:
    f.write('Hello')
print('Exists:',os.path.exists(file))
print('Size:',os.path.getsize(file))
new = p/'os_renamed.txt'
os.replace(file,new)
print('Renamed:',os.path.basename(new))
