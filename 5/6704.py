for n in range (0,1_000_000):
    binarnoe = bin(n)[2:]
    if n % 2 == 1:
        binarnoe = binarnoe.replace('0','1').replace('1','0')
    binarnoe = binarnoe.replace('0','00').replace('1','11')
    r = int(binarnoe,2)
    if r > 60:
        print(n)
        break
