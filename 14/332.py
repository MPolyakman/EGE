n = ((4**2014)+(2**2015)-8)
x = ''
while n > 0:
    x = str(n % 2) + x
    n = n // 2
print(x.count('1'))