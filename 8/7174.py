from itertools import*
cnt =0
for word in permutations('глубина'):
    word = ''.join(word)
    if word[word.find('г')-1] == 'а' or word[word.find('г')-1] == 'и':
        cnt += 1
print(cnt)