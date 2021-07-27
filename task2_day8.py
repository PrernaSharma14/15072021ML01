
x = 0
def mm():
    while True:
        global x
        if x%2 == 1:
            yield x
        x +=1
yy = mm()
while True:
    print(next(yy))






