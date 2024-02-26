# isdigit - проверяет, состоит ли строка целиком из цифр
# isalpha - проверяет, состоит ли строка целиком из букв
x = '123'
print(x.isdigit()) # True
print(x.isalpha()) # False
y = 'Hello'
print(y.isdigit()) # False
print(y.isalpha()) # True
z = 'Номер1'
print(z.isdigit()) # False
print(z.isalpha()) # False