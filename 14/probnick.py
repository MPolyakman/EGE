f = 3*(3125**9)+2*(625**8)-4*(625**7)+3*(125**6)-2*(25**5)-2024
r = ''
alff = '0123456789qwertyuiopasdfghjklzxcvbnm'
alf = [letter for letter in alff]
while f > 0:
    r = alf[f%25] + r
    f = f//25
print(r.count('0'))
