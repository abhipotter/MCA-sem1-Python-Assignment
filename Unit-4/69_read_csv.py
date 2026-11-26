import csv
from pathlib import Path
p = Path(__file__).with_name('students.csv')
with open(p,'r',newline='',encoding='utf-8') as f:
    for row in csv.reader(f):
        print(' | '.join(row))
