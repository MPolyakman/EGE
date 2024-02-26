from itertools import*
counting = 0
for i in product('капн',repeat = 6):
    word = ''.join(i)
    if 'кк' not in word and 'аа' not in word and 'пп' not in word and 'нн' not in word\
        and word.count('а') == 2 and word.count('к') == 2 and word.count('п') == 1 and word.count('н') == 1:
        counting += 1
print(counting)

cnt = 0
for i in permutations('капкан'):
    i = ''.join(i)
    if 'аа' not in i and 'кк' not in i:
        cnt += 1
print(cnt/4)