for a in range (0, 10000):
    cnt = 1
    for x in range (0,500):
        for y in range(0,500):
            f = (x < a) or (y < a) or ((x + (2 * y)) > 50)
            if f == False:
                cnt = 0
                break
        if cnt == 0:
            break
    if cnt == 1:
        print(a)
        break