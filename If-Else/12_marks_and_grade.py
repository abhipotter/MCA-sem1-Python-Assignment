p = float(input('Physics: '))
c = float(input('Chemistry: '))
b = float(input('Biology: '))
m = float(input('Mathematics: '))
cs = float(input('Computer: '))
if min(p,c,b,m,cs) < 0 or max(p,c,b,m,cs) > 100:
    print('Invalid marks')
else:
    per = (p+c+b+m+cs)/5
    if per >= 90:
        grade = 'A'
    elif per >= 80:
        grade = 'B'
    elif per >= 70:
        grade = 'C'
    elif per >= 60:
        grade = 'D'
    elif per >= 40:
        grade = 'E'
    else:
        grade = 'F'
    print('Percentage:', per)
    print('Grade:', grade)
