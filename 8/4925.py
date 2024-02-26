cou = 0
for i in range(int('1000000', 7), int('10000000', 7)):
    r = ''
    while i > 0:
        r = str(i % 7) + r
        i = i // 7
    if r[0] != '3' and r[0] != '5' and ('22' not in r or '44' not in r):
        cou += 1
print(cou)
