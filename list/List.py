# Создадим список а
a = []
print(type(a))
# Создадим список b
b = list('Hello')
print(b)
# Создадим список c
c = [1,2,5]
print(c)

# Создадим список d
d = [1,2,5,'hello',[11,22,33]]
print(d)

# Выведем 2 по счету элемент
print(d[1])

# Выведем список [11,22,33] из списка d
print(d[4])
print(d[-1])

# Выведем из список [11,22,33] в списке d 22
print(d[4][1])

a = [23, 57, 77, 23, 80, 62, 23]
print(a.count(23)) # 3
print(max(a)) # 80
print(min(a)) # 23
print(a.count(max(a))) # 1
print(len(a)) # 7
print(sum(a)) # сумма всех элементов а