res = [0]*100000
answ = []
for n in range(1,10000):
    r = bin(n)[2:]
    r = r + bin(n%4)[2:]
    r = int(r,2)
    res[r] = 1
for i in range(49,100000):
    srez = sum(res[i-49:i])
    answ.append(srez)
print(max(answ))

