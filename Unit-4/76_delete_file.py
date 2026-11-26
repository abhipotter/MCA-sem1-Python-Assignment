import os
from pathlib import Path
p = Path(__file__).with_name('delete_demo.txt')
p.write_text('Temporary file',encoding='utf-8')
if os.path.exists(p):
    os.remove(p)
    print('File deleted')
