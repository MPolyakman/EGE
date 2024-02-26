from itertools import*
cnt = 0
# for i in product('тимашевск', repeat = 9):
#     i = ''.join(i)
#     if i.count('т') == 1 and i.count('и') == 1 and i.count('м') == 1 and i.count('а') == 1 and i.count('ш') == 1\
#             and i.count('е') == 1 and i.count('в') == 1 and i.count('с') == 1 and i.count('к') == 1:
#         i = i.replace('т','1').replace('м','1').replace('ш','1').replace('в','1').replace('с','1').replace('к','1')
#         i = i.replace('и','0').replace('а','0').replace('е','0')
#         if i[0] == '1' and i[-1] == '1' and '000' in i:
#             cnt += 1
# print(cnt)

for i in permutations('тимашевск'):
    i = ''.join(i)
    i = i.replace('т','1').replace('м','1').replace('ш','1').replace('в','1').replace('с','1').replace('к','1')
    i = i.replace('и','0').replace('а','0').replace('е','0')
    if i[0] == '1' and i[-1] == '1' and '000' in i:
        cnt += 1
print(cnt)
