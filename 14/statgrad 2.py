for x in range(40):
    for y in range(40):
        num = 5 *(40**8) + 7*(40**7)+ x*(40**6)+ 6*(40**5)+ 9*(40**4)+ 2*(40**3)+ y*(40**2)+ 1*(40**1)+ 9*(40**0)
        if num%39 == 0 and ((y*40 + x)**0.5)% 1 == 0:
            print(y*40 + x)
