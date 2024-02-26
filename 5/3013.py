for n in range(1,256):
    bi = bin(n-1)[2:].rjust(8,'0')
    bi = bi.replace('0','*')
    bi = bi.replace('1','0')
    bi = bi.replace('*','1')
    if int(bi,2) == 204:
        print(n)
        break