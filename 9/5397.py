f = open('9-162.txt')
cnt = 0
for string in f:
    stroka = sorted(int(x) for x in string.split())
    if ((stroka[0] + stroka [1]) == (stroka[2] + stroka [3])) or (stroka[0] + stroka [2] == stroka[1] + stroka[3]) or \
            ((stroka[0] + stroka[3]) == (stroka[1] + stroka[2])):
        if (stroka[3] - stroka[0]) < ((stroka[1] + stroka[2])- stroka[3]):
            cnt += 1
print(cnt)