print("x y z w f")
for x in range (2):
    for y in range (2):
        for z in range (2):
            for w in range (2):
                f = ((y <= x) and (not(z)) and w)
                if f == 1:
                    print(x,y,z,w,f)
#w x y z