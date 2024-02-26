from itertools import*
words = ['1']
for word in product('АВИКПРЧЫ',repeat=5):
    word = ''.join(word)
    words.append(word)
for id in range(len(words)-1):
    if id%5 ==0:
        words[id] = '0'
while '0' in words:
    words.remove('0')
for answer in words:
    for letter in answer:
        if answer.count(letter) != 1 or letter not in 'ПРВЧК':
            break
    else:
        print(words.index(answer))
        break

