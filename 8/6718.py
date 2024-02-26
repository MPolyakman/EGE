from itertools import*
cnt = 0
for i in product('екмопртью',repeat=5):
    word = ''.join(i)
    cnt += 1
    if word[0] != 'ь' and word.count('к') == 2 and cnt%2 == 1:
        print(cnt)