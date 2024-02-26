def three(n):
    r = ''
    while n > 0:
        r = str(n%3) + r
        n = n // 3
    return r

for n in range (1,10000):
    r = three(n)
    if n % 2 == 0:
        r = '1' + r + '00'
    else:
        r = r + three(sum(map(int,list(r))))
    if int(r,3) >  168:
        print(n)
        break

