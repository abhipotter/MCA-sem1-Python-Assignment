from pathlib import Path
import shutil
p = Path(__file__).parent
shutil.copyfile(p/'sample.txt',p/'copy.txt')
print('File copied')
