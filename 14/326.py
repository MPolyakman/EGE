for s in range (2,9):
    n = 30
    r = ''
    while n > 0:
        r = str(n % s) + r
        n = n // s
    if len(r) == 3:
        print(s)
        break