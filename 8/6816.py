from itertools import*
cnt = 0
for i in product('адуч', repeat=5):
    word = ''.join(i)
    word2 = word.replace('а','1').replace('у','1')
    if word2[0] == '1':
        cnt += 1
        if word == 'удача':
            break
print(cnt)