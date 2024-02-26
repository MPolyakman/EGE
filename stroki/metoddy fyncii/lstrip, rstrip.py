# x.rstrip, x.lstrip - удаление пробельных символов в начале или конце строки
x = '  Привет'
x = x.lstrip()
print(x) # Привет
y = 'Привет  '
y = y.rstrip()
print(y) # Привет