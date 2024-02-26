from itertools import*
cnt = 0
for i in product('01234567',repeat=8):
    i = ''.join(i)
    i = i.replace('2','0').replace('4','0').replace('6','0')
    i = i.replace('3', '1').replace('5', '1').replace('7', '1')
    if i[0] == '1' and i[-1] == '1' and '00' in i and '000' not in i:
        cnt += 1
print(cnt)