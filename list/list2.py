# Добавим в список число 5
# x.append(y) - добавляет в список x элемент y
a = []
a.append(5)

# Создать список из четных чисел от 1 до 100

c = []
for i in range(2,101,2):
    c.append(i)
print(c)

k = [i for i in range(2,101,2)]
print(k)

# Создать список из четных чисел от 1 до 100 кратных 3

p = []
for i in range(2,101,2):
    if i%3==0:
        p.append(i)
print(p)

# Создать список из четных чисел от 1 до 100 кратных 3

p = [i for i in range(2,101,2) if i%3==0]
print(p)



h = [i*3 for i in 'list' if i!='i']
print(h)


h = [int(i)*3 for i in '56789' if i!='6']
print(h)
