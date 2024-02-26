from itertools import*
cnt=0
for word in product('аглоь',repeat=5):
    word = ''.join(word)
    cnt += 1
    if word == 'ольга':
        print(word, cnt)
        break
