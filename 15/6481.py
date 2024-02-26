p = [i for i in range(106,219)]
q = [i for i in range(132,389)]
r = [i for i in range(183,256)]

answer = []
for  a1 in range(0,500):
    for a2 in range(a1, 500):
        cnt = 1
        for x in range(0,500):
            if ((not((x in q) <= ((x in p) or (x in r)))) <= ((a1 <= x <= a2) <= (not(x in q)))) == False:
                cnt = 0
                break
        if cnt == 1:
            answer.append(a2-a1)
print(min(answer))
