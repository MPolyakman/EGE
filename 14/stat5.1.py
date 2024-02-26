for p in range(5,37):
    for x in range(0,p):
        for y in range(0,p):
            if (1*p+2)*(3*p+4) == (x*(p**2))+(y*p)+2:
                print(y*p+x)