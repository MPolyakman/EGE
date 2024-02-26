from itertools import*
words = 0
for i in product('ёиклнос',repeat = 5):
    words += 1
    if i[0] != 'о' and i[1] == 'к' and i.count('ё') >= 2:
        print(words)