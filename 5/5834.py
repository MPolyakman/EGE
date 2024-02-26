for n in range(1,100_000_000):
    r = hex(n)[2:]
    if int(r,16)%2 == 0:
        r = r + 'f'
    else:
        r = r + '0'
    summm = 0
    for letter in r:
        summm += int(letter,16)
    r = r + hex(summm%16)[2:]
    summm = 0
    for letter in r:
        summm += int(letter, 16)
    r = r + hex(summm % 16)[2:]
    if r.count(max(r)) == r.count(min(r))*5:
        print(n)
        break