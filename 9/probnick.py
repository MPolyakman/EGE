f = open('probnick.txt')
answer = 0
for string in f:
    answer+=1
    stroka = list(map(int,string.split()))
    cnt = 0
    for num in stroka:
        if stroka.count(num) == 2:
            cnt +=1
    stroka.sort()
    if cnt == 4 and stroka.count(max(stroka))==1 and stroka[0]*stroka[-1] > stroka[1]+stroka[2]+stroka[3]+stroka[4]:
        print(answer)
        break
