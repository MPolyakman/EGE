n = ((9**8)+(3**5)-2)
x = ''
while n > 0:
    x = str(n%3) + x
    n = n//3
print(x.count('2'))