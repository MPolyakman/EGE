n = ((4**2016)+(2**2018)-(8**600)+6)
x = ''
while n > 0:
    x = str(n % 2) + x
    n = n // 2
print(x.count('1'))