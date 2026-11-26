s = float(input('Basic salary: '))
if s < 0:
    print('Invalid salary')
else:
    if s <= 10000:
        hra, da = s*0.20, s*0.80
    elif s <= 20000:
        hra, da = s*0.25, s*0.90
    else:
        hra, da = s*0.30, s*0.95
    print('Gross salary:', round(s+hra+da,2))
