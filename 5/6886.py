for n in range (1,10000):
    operand = n
    r = ''
    summa = 0
    while operand > 0:      # число н в троичной
        r = str(operand%3) + r
        summa += operand%3
        operand = operand//3
    # for i in r:
    #     suma += int(i)
    # peremen2 = n
    # while peremen2 > 0:
    #     suma += peremen2 % 3
    #     peremen2 = peremen2 // 3
    if summa % 3 == 0:
        r = '20' + str(r)
    else:
        r = '10' + str(r)
    if int(r,3) < 100:
        print(n,int(r,3))