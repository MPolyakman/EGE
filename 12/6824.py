for n in range(4,10_000):
    stroka = '1' + n * '8'
    while '18' in stroka or '388' in stroka or '888' in stroka:
        if '18' in stroka:
            stroka = stroka.replace('18','8',1)
        if '388' in stroka:
            stroka = stroka.replace('388','81',1)
        if '888' in stroka:
            stroka = stroka.replace('888', '3',1)
    if stroka.count('1') == 3:
        print(n)
        break