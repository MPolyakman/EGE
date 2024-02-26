from itertools import*
cnt = 0
for i in product('01234567',repeat=8):
    i = ''.join(i)
    if i[0] != '0':
        if int(i[0])% 2 == 0 and int(i[-1])% 2 == 0:
            i = i.replace('3','1').replace('5','1').replace('7','1')
            if '111' in i:
                cnt += 1
print(cnt)