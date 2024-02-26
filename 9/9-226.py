f = open('9-226 (1).txt')
for string in f:
    stroka = sorted(int(x) for x in string.split())
    cnt = 0
    for number in stroka:
        if stroka.count(number) == 2 and stroka.count(number) < 3:
            cnt += 1
    if cnt == 4 and stroka.count(stroka[-1]) == 1:
        print(stroka)
        print(sum(stroka))