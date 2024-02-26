for a in reversed(range(0,500)):
    cnt = 1
    for x in range(0,500):
        for y in range(0,500):
            if (((x + 2*y) > a) or (y < x) or (x < 30)) == False:
                cnt = 0
                break
        if cnt == 0:
            break
    if cnt == 1:
        print(a)
        break