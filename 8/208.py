from itertools import*
cnt = 0
for i in product('ABCX',repeat=5):
    word = ''.join(i)
    if word.find('X') in [-1,4]:
        cnt+=1
print(cnt)