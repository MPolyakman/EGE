from itertools import *
answer = set()
for word in permutations('ПРОСТО'):
    word = ''.join(word)
    for id in range(5):
        if word[id] == word[id+1]:
            break
    else:
        answer.add(word)
print(len(answer))
