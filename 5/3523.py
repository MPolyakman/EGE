for n in range(1,1001):
    n2 = str(n) + str(n)[-1]
    bi = bin(int(n2))[2:]
    if bi.count('1') % 2 != 0:
        bi = bi + '1'
    else:
        bi = bi + '0'
    if int(bi,2) > 413:
        print(n)
        break