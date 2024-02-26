for i in range(10000,100000):
    n1 = int(str(i)[0]) + int(str(i)[2]) + int(str(i)[4])
    n2 = int(str(i)[1]) + int(str(i)[3])
    if n1 >= n2:
        n3 = str(n2) + str(n1)
    else:
        n3 = str(n1) + str(n2)
    if n3 == '723':
        print(i)
        break
