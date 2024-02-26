cnt = 0
for i in range(100,1000000):
    i = oct(i)[2:]
    if len(i) == 5 and i.count('0') <= 1 and i.count('1') == 0 and i.count('2') <= 1 and i.count('3') <= 1 and i.count('4') <= 1 and i.count('5') <= 1 and i.count('6') <= 1 and i.count('7') <= 1:
        newi = i.replace('2','0').replace('4','0').replace('6','0')\
            .replace('3','1').replace('5','1').replace('7','1')
        if '00' not in newi and '11' not in newi:
            print(i)
            cnt += 1
print(cnt)