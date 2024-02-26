for x in range(6, 1000):
    f = (4*(x*(x-1))+((x-1)**2))
    if f > 1500:
        print(x)
        break