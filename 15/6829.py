for a in range (1,100000):
    cnt = 1
    for x in range(1, 1000):
        if (((a + x) < 123) <= ((x % 5 == 0) <= (x % 7 != 0))) == False:
            cnt = 0
            break
    if cnt == 1:
        print(a)
        break