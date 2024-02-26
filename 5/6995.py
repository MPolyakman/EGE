for n in range(1,1000):
    r = bin(n)[2:]
    if r.count('1') % 2 == 0:
        r = r + r[-2:]
    else:
        r = r + r[-2:][::-1]
    r = int(r,2)
    if r > 154 and r < 170:
        print(n)



