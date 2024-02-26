stroka = input()
posle = ''
k = 0
for i in stroka:
    if k % 3 != 0:
        posle += i
    k += 1
print(posle)