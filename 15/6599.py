for a in range(1,1000):
    cnt = 1
    for x in range(1,1000):
        if ((((x & 103) == 0) and ((x & 94) != 0)) <= ((x & a) != 0)) == False:
            cnt = 0
            break
    if cnt == 1:
        print(a)
        break
