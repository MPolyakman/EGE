from itertools import*
cnt = 0
for i in permutations('abcdef',4):
    i = ''.join(i)
    i = i.replace('a','1').replace('b','1').replace('d','1').replace('e','1')
    if '11' not in i:
        cnt += 1
print(cnt)