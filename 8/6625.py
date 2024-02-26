from itertools import*
cnt = 0
for i in permutations('хочунабюджет'):
    word = ''.join(i).replace('о','1').replace('у','1').replace('а','1').replace('ю','1').replace('е','1')
    if '11111' not in word:
        cnt += 1
print(cnt)
