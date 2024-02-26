for n in reversed(range(1,10000)):
    newn = n
    troika = ''
    while newn > 0:
        troika = str(newn % 3) + troika
        newn = newn // 3
    if n % 3 == 0:
        troika = '1' + troika + '02'
    else:
        peremen = (n % 3)*4
        dobavok = ''
        while peremen > 0:
            dobavok = str(peremen % 3) + dobavok
            peremen = peremen // 3
        troika += dobavok
    r = int(troika,3)
    if r < 199:
        print(n)
        break