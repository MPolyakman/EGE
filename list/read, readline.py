f = open('9-226.txt')
# s = f.readline() # 1 строка считывается в s
k = f.read() # считывает файл
print(k)
print('*'*100)
f.close()
f = open('9-226.txt')
m = f.readline()
print(m)
f.close()