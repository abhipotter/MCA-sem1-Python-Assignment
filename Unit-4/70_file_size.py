import os
from pathlib import Path
p = Path(__file__).with_name('sample.txt')
print('Size:',os.path.getsize(p),'bytes')
