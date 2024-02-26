schet = 0
for i in range(0,(10**10)+1,4546):
    if str(i)[0] == '8' and str(i)[-2:] == '06' and '80' in str(i)[1:-2]:
        if schet % 60 == 0:
            print(i, i // 4546,schet)
        schet += 1