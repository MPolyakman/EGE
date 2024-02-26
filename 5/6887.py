answers = []
for n in range (11,10000):
    r = ''
    while n > 0:
        r = str(n % 3) + r
        n = n//3
    new = r.replace('2','0').replace('4','0').replace('6','0').replace('8','0').replace('3','1').replace('5','1').replace('7','1').replace('9','1')
    if new.count('1') < new.count('0'):
        r = '22' + r
    else:
        r = '11' + r
    if int(r,3) > 100:
        print(int(r,3))