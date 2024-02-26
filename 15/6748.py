for a in range(0, 100):
    cnt = 1
    for x in range(0, 1000):
        for y in range(0, 1000):
            if (((x * y) < a) or (x < y) or (9 < x)) == False:
                cnt = 0
                break
        if cnt == 0:
            break
    if cnt == 1:
        print(a)
        break
