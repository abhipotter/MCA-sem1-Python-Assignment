from pathlib import Path
import re
p = Path(__file__).parent
file = p/'replace_demo.txt'
if not file.exists():
    file.write_text((p/'sample.txt').read_text(encoding='utf-8'),encoding='utf-8')
old = input('Word to replace: ')
new = input('New word: ')
if old:
    s = file.read_text(encoding='utf-8')
    s = re.sub(r'\b'+re.escape(old)+r'\b',lambda m: new,s)
    file.write_text(s,encoding='utf-8')
    print(s)
