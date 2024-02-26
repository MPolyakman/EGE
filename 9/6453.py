f = open('9-210.txt')
cnt = 0
for string in f:
    stroka = sorted([int(x) for x in string.split()])
    if stroka.count(stroka[0]) == 1:
        if len(set(stroka)) < 6:
            if stroka[0] + stroka[-1] <2*((stroka[1]+stroka[2]+stroka[3]+stroka[4])/4):
                cnt += 1
print(cnt)