n = ((4**2015) + (8**405) - (2**150) - 122)
x = ''
while n > 0:
    x = str(n % 2) + x
    n = n // 2
print(x.count('1'))