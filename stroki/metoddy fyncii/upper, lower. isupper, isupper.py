# x.upper(), x.lower() - преобразуют строку в верхний или нижний регистр
x = 'Привет'
x = x.upper()
print(x)
x = x.lower()
print(x)
y = 'ПРИВЕТ'
print(y.isupper()) # True
print(y.islower()) # False
z = 'Привет'
print(z.isupper()) # False
print(z.islower()) # False