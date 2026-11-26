x = 10

def show():
    global x
    y = 5
    x += 2
    print('Local:',y)

show()
print('Global:',x)
