file = open('9-222.txt')
cnt = 0
for stroka in file:
    cnt += 1
    a = [int(x) for x in stroka.split()]
    b = [x for x in a if a.count(x) == 2]
    c = [x for x in a if a.count(x) == 1]
    if len(b) == 2 and b[0] >= sum(c)/4:
        print(cnt)
