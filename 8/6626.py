from itertools import*
words = 0
cnt = 0
for i in product('ьрплеа',repeat = 5):
    i = ''.join(i)
    words += 1
    if i[-1] == 'ь':
        cnt += 1
    if words == 387:
        print(cnt)
        break