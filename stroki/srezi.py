# Выведем третью буквы слова "здравствуйте"
# Способ 1
print("здравствуйте"[2])
# Спасоб 2
x = "здравствуйте"
print(x[2])
# Выведем четвертую цифру числа y
y = 58248
# Срезы не применимы к int
print(str(y)[3])
# Выведем вторую цифру числа умноженную на 5
print(int(str(y)[1])*5)
# Выведем с третьего по седьмой символ включительно в слове "здравствуйте"
print(x[2]+x[3]+x[4]+x[5]+x[6])
print(x[2:7])
# Выведем со второго по предпоследний элемент(включительно) через символ
print(x[1:-1:2])
# Выведем с начало до 6 символа (включительно)
print(x[:6])
# Выведем с 4 элемента до конца
print(x[3:])
print(x[2:9:])
print(x[::])
# Выведем слова задом наперед
print(x[::-1])
# Проверим является ли слово палиндромом
y = 'шалаш'
print(y==y[::-1])