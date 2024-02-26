spisok = []
for n in range(12,100_0):
    r = ''
    i = n
    while i > 0 :
        r = str(i %12) + r
        i = i//12
    if n % 12 == 0:
        r = r + r[-2:]
    else:
        p = (n%12)*9
        ostatok = ''
        while p > 0:
            ostatok = str(p%12) + ostatok
            p = p//12
        r = r + str(ostatok)
    if int(r,12) > 300:
        spisok.append(int(r,12))
print(min(spisok))