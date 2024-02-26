# cnt = 0
# alf = '0123456789ab'
# for i in range(int('1000000',12),int('10000000',12)):
#     r = ''
#     while i > 0:
#         r = alf[i % 12] + r
#         i = i // 12
#     r = r.replace('3','0').replace('6','0').replace('9','0').replace('2','1').replace('4','1')\
#         .replace('5','1').replace('7','1').replace('8','1').replace('a','1').replace('b','1')
#     if '00' not in r and '11' not in r:
#         cnt += 1
# print(cnt)

from itertools import*
cnt = 0
for i in product('нк',repeat=7):
    i = ''.join(i)
    if 'нн' not in i and 'кк' not in i:
        if i[0] == 'н':
            cnt += (8**4)*(4**3)
        else:
            cnt += (8**3)* (4**3)*3
print(cnt)