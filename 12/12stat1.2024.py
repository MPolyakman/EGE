def suma_of_numbers(s):
    suma = 0
    for number in str(s):
        suma += int(number)
    return suma

def sum_num(stroka):
    return sum(map(int,list(stroka)))

def simple(n):
    for delitel in range(2,n):
        if n % delitel == 0:
            return False
    else:
        return True
spisok = []
for n in range(0,100):
    for j in range(0,100):
        a = '0' + n*'1' + j*'2'
        if len(a) >= 45:
            b = a
            while '01' in b or '02' in b:
                b = b.replace('02','1110',1)
                b = b.replace('01','220',1)
            if simple(sum_num(b)):
                spisok.append(sum_num(a))
print(min(spisok))

