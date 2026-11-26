import os
from pathlib import Path
p = Path(__file__).with_name('demo_folder')
os.makedirs(p,exist_ok=True)
(p/'hello.txt').write_text('Hello',encoding='utf-8')
print(os.listdir(p))
