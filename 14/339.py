n = abs((4**812) + (8**800) - (2**3125) - (8**65) - (4**312) + 130)
x = ''
while n > 0:
    x = str(n % 2) + x
    n = n // 2
print(x.count('0'))
print((4**812) + (8**800) - (2**3125) - (8**65) - (4**312) + 130)