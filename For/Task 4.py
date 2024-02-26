# вывести строку через 1 элемент используя индекс
slovo = input()
for i in range(0, len(slovo), 2):
    print(slovo[i])
print('*****')
for i in reversed(range(0, len(slovo), 2)):
    print(slovo[i])