list = []
for n in range (4,1000):
    stroka = '1' + '2'* n
    while '12' in stroka or '322' in stroka or '222' in stroka:
        if '12' in stroka:
            stroka = stroka.replace('12','2',1)
        if '322' in stroka:
            stroka = stroka.replace('322','21',1)
        if '222' in stroka:
            stroka = stroka.replace('222','3',1)
    list.append(len(stroka))
print(max(list))
