# Сколько существует шестнадцатеричных трёхзначных чисел, в которых все цифры различны и никакие две чётные или две нечётные цифры не стоят рядом?
cnt = 0
for i in range (int('100',16),int('1000',16)):
    i = hex(i)[2:]
    if i[0] != i[1] and i[1] != i[2] and i[0] != i[2]:
        for letter in i:
            if int(letter,16) % 2 == 0:
                i = i.replace(letter,'0')
            else:
                i = i.replace(letter,'1')
        if '00' not in i and '11' not in i:
            cnt += 1
print(cnt)