answer = []
for n in range(1,1000):
    r = bin(n)[2:]
    r = r[1:]
    if r.count('1')%2 == 0:
        r = '10' + r
    else:
        r = '1' + r + '0'
    r = int(r,2)
    if r < 450:
        answer.append(r)
print(max(answer))