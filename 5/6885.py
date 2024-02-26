alf = '0123456789abcde'
list = []
for a in range(15,100000):
    n = a
    r = ''
    while n > 0:
        r = alf[n%15] + r
        n = n//15
    if a % 15 == 0:
        r = r +r[:2]
    else:
        d = (a%15)*13
        plus = ''
        while d > 0:
            plus = alf[d%15] + plus
            d = d//15
        r = r + plus
    if int(r,15) > 700:
        list.append(int(r,15))
print(min(list))