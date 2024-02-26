# вводится строка вывести ее же кроме элементов индексов кратных трём
x = input()
slovo = ''
for i in range(len(x)):
    if i % 3 != 0:
        print(x[i], end = '')