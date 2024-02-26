n = ((4**512) + (8**512) - (2**128) - 250)
x = ''
while n > 0:
    x = str(n % 2) + x
    n = n // 2
print(x.count('0'))