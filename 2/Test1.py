print("x y z w f1   f2")
for x in range (2):
    for y in range (2):
        for z in range (2):
            for w in range (2):
                f1 = ((x == y) and (w <= z))
                f2 = ((x <=  y) <= (w == z))
                if f1 == 1 and x == 0 and w == 1:
                    print(x,y,z,w,f1,f2)
    # y w x z