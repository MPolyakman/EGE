from itertools import*
number_of_word= 0
for word in product('авест',repeat=5):
    word = ''.join(word)
    number_of_word += 1
    print(word,number_of_word)
    if word == 'света':
        print(word, number_of_word)
        break