answer =[]
for n in range(1,10000):
    r = bin(n)[2:]
    if n%3==0:
        r = r.replace('0','11')
    if n%3!=0:
        r = r.replace('1','10')
    r = int(r,2)
    if r <= 161:
        answer.append(r)
print(max(answer))