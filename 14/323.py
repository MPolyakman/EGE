alf = '0123456789abcdefghijklmnopqrstuvwxyz'
for n in range(2,37):
    x = 94
    y = ''
    while x > 0:
        y = alf[x%n] + y
        x //= n
    if y[:2] == '23':
        print(n)
        break