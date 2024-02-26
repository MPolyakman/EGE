from itertools import*
cnt = 0
for i in product('аклош',repeat=5):
    word = ''.join(i)
    cnt += 1
    if word == 'школа':
        break
print(cnt)