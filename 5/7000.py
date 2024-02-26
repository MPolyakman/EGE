def summ(n):
    output = 0
    for letter in str(n):
        output += int(letter)
    return output
cnt = 0
for n in range(100_000_000, 1_000_000_000):
    if summ(n) < 21:
        r = bin(summ(n))[2:]
        if r.count('1') % 2 == 0:
            r = '1' + r + '00'
        else:
            r = '10' + r + '1'
        if int(r,2) == 21:
            cnt += 1
print(cnt)