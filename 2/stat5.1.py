print('x','y','w','z','f1','   f2')
for x in 0, 1:
    for y in 0, 1:
        for w in 0, 1:
            for z in 0, 1:
                f1 = ((x or (not (y))) <= (w == z))
                f2 = ((x or (not (y))) == (z <= w))
                if f1 == 0 and z == 1:
                    print(x,y,w,z,f1,f2)