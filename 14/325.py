for s in range (4,13):
    r = ''
    n = 71
    while n > 0:
        r = str(n % s) + r
        n = n // s
    if r[-2:] == '13':
        print(s)
        break