answer = []
for n in range (1,1000):
    new = n
    four = ''
    while new > 0:
        four = str(new % 3) + four
        new = new//3
    if n % 4 == 0:
        four = four + four[-3:]
    else:
        ostatok = (n % 4) *4
        fournew = ''
        while ostatok > 0:
            fournew = str(ostatok % 3) + fournew
            ostatok //= 3
        four = four + fournew
    four = int(four,3)
    if four < 127:
        answer.append(four)
print(max(answer))