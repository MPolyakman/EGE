from itertools import*
cnt = 0
for i in product('пролив',repeat=6):
    word = ''.join(i)
    if word.count('п') >= 1:
        cnt += 1
print(cnt)