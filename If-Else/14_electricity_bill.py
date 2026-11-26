u = float(input('Units: '))
if u < 0:
    print('Invalid units')
else:
    if u <= 50:
        bill = u*0.50
    elif u <= 150:
        bill = 25 + (u-50)*0.75
    elif u <= 250:
        bill = 25 + 75 + (u-150)*1.20
    else:
        bill = 25 + 75 + 120 + (u-250)*1.50
    bill = bill + bill*0.20
    print('Total bill: Rs.', round(bill,2))
