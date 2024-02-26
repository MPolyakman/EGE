for n in range(1,10000):
    r = bin(n)[2:]
    if r.count('1') > r.count('0'):
        r = r+'0'
    else:
        r='11' + r
    r = int(r,2)
    if r > 2019:
        print(n)
        break