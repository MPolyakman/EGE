for n in range(1,10000):
    n2 = bin(n)[2:]
    if n % 2 == 0:
        n2 = n2 + '0'
    else:
        n2 = n2 + '1'
    if n2.count('1') % 2 == 0:
        n2 = n2 + '0'
    else:
        n2 = n2 + '1'
    r = int(n2,2)
    if r > 2023 and r < 2030:
        print(r)
