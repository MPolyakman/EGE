# x.split('y') - пересоздаем строку х в список разделяя y
a = '11 22 33 44 55 66 77 77'
b = a.split() # по умолчанию исп-ся пробел -['11', '22', '33', '44', '55', '66', '77']
print(b)
c = [int(i) for i in b]
print(c)
d = [int(i) for i in a.split()]
print(*d)
print(d.count(77)) # 2
print(d.count(11)) # 1
print(d.count(12131)) # 0

lll = '120540624501240124041041'
lll = lll.replace('0','0 ')
op = lll.split()
print(op)