for n in range (1,1000):
    r = ''
    while n > 0:
        r = str(n % 3) + r
        n = n//3
    if n % 3 == 0:
        r = r + r[-2:]
    else:
        ost = (n % 3)*5
        ost3 = ''
        while ost > 0:
            ost3 = str(ost % 3) + ost3
            n = n//3
        r = r + ost3
    if int(r,3) > 133:
        print(int(r,3))
        break