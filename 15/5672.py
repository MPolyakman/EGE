b = [i for i in range(10,41)]
answer = []
for a1 in range(0,100):
    for a2 in range(a1,100):
        a = [i for i in range(a1,a2 + 1)]
        cnt = 1
        for x in range(0, 100):
            if ((x in a) or ((x in b)) <= (not(x % 6 == 0))) == False:
                cnt = 0
                break
        if cnt == 1:
            answer.append(a2-a1)
            print(a1,a2)
print(min(answer))
