# Вводится строка. Вывести отдельно в трёх строках все цифры, все буквы и все символы по отдельности
stroka = input()
bykvi = ''
cifry = ''
simvoly = ''
for i in stroka:
    if i.isalpha():
        bykvi += i
    elif i.isdigit():
        cifry += i
    else:
        simvoly += i
print(cifry)
print(bykvi)
print(simvoly)