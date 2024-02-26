for i in reversed(range(4,10000)):
    newn = 0
    n = '5' + '2'*i
    while '52' in n or '2222' in n or '1122' in n:
        if '52' in n:
            n = n.replace('52','11')
        if '2222' in n:
            n = n.replace('2222','5')
        if '1122' in n:
            n = n.replace('1122','25')
    for letter in n:
        newn += int(letter)
    if newn == 64:
        print(i)
        break