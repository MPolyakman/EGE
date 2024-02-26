alf = '0123456789abcdefghijklmnopqrstuvwxyz'
for n in range(2,37):
    x = 30
    y = ''
    while x > 0:
        y = alf[x%n] + y
        x //= n
    if y[-1] == '0' and len(y) == 4:
        print(n)
        break