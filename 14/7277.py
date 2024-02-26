# zxyx9 + xy748 = wzx61
alf = sorted('0123456789asdfghjklwertyuiopzxcvbnm')
for p in range(10,100):
    for x in range(p):
        for y in range(p):
            for z in range(p):
                for w in range(p):
                    if 9*(p**0) + x*(p**1) + y*(p**2) + x*(p**3) + z*(p**4) + 8*(p**0) + 4*(p**1) + 7*(p**2) + y*(p**3) + x*(p**4) == 1*(p**0) + 6*(p**1) + x*(p**2) + z*(p**3) + w*(p**4):
                        print(int(f'{alf[x]}{alf[y]}{alf[z]}{alf[w]}',p))
                        exit()