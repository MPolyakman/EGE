for n in range(1, 1000):
    r = bin(n)[2:]
    ind = r.rfind('0')
    if ind != -1:
        r = r[:ind] + r[:2] + r[ind+1:]
        r = r[::-1]
        if int(r, 2) == 123:
            print(n, r)
            break


