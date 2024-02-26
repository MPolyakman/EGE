f = open('9-224.txt')
repeated = []
answer = 0
for string in f:
    stroka = sorted(int(x) for x in string.split())
    cnt = 0
    for number in stroka:
        if stroka.count(number) == 2:
            repeated.append(number)
            cnt += 1
        if stroka.count(number) == 1:
            unrepeated = number
    if cnt == 4 and unrepeated > min(repeated) and unrepeated < max(repeated):
        answer += 1
print(answer)