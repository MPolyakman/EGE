from itertools import*

cnt = 0
for word in product('чистыйразум',repeat=5):
    word = ''.join(word)
    if word.count('й') <= 1:
        cnt += 1
print(cnt)