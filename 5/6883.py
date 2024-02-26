spisok = []
for n in range(5,100_000):
    i = n
    r = ''
    while i > 0:
        r = str(i%5) + r
        i = i//5
    if n %5 == 0:
        r = r + r[-2:]
    else:
        p = (n%5)*7
        ostatok = ''
        while p > 0:
            ostatok = str(p%5) + ostatok
            p = p//5
        r = r + str(ostatok)
    if int(r,5) > 200:
        spisok.append(int(r,5))
print(min(spisok))