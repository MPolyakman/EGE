#написать программу используя цикл while для определения количества цифр в натуральном числе Н
N = int(input())
dlina = 0
while N > 0:
    dlina += 1
    N //= 10
print(dlina)