alf = '0123456789abcdefghijklmnopqrstuvwxyz'
for n in range(3,37):
    x = 86
    y = ''
    while x > 0:
        y = alf[x%n] + y
        x //= n
    if y[-2:] == '22':
        print(n)
        break