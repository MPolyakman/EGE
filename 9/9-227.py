file = open('9-227 (1).txt')
answer = 0
for string in file:
    cnt = 0
    stroka = sorted(int(x) for x in string.split())
    for number in stroka:
        if stroka.count(number) == 2:
            cnt += 1
    if cnt == 2 and (stroka[3] + stroka[2]) > (2*(stroka[0]+stroka[1])) and stroka[3] % stroka[0] != 0:
        answer += 1
print(answer)
