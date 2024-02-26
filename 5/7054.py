def six(iter_n):
    r = ''
    while iter_n > 0:
        r = str(iter_n % 6) + r
        iter_n = iter_n // 6
    return r

answer = []


for n in range(1,1000):
    r = six(n)
    if n % 3 == 0:
        r = r + r[:2]
    else:
        r = r + six(10*(n % 3))
    if int(r,6) > 680:
        answer.append(int(r,6))
print(min(answer))
