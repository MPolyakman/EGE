cou = 0
for i in range (0,100000):
    r = oct(i)[2:]
    if len(r) == 4 and i % 4 == 0:
        cou += 1
print(cou)