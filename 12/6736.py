for n in range(101,10000):
    inter = '5' * n
    while '555' in inter or '11' in inter or '2' in inter:
        if '555' in inter:
            inter = inter.replace('555','1',1)
        if '11' in inter:
            inter = inter.replace('11', '25', 1)
        if '2' in inter:
            inter = inter.replace('2', '5', 1)
    if inter == '15':
        print(n)
        break