for a in reversed(range(1,500)):
    for x in range(500):
        for y in range(500):
            if not (((4 * x + y) > 115) or (x > 3 * y) or (x + 4 * y < a)):
                print(a)
                exit()