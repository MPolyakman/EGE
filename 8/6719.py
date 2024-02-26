from itertools import*
cnt = 0
for i in product('агмнсту',repeat=6):
    word = ''.join(i)
    cnt += 1
    if word[0] != 'у' and word.count('м') == 2 and word.count('г') <= 1:
        print(cnt)