print('x y z w u')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                for u in range(2):
                    f = (((x <= y) and (z == (not(w)))) <= (u == (x or z)))
                    if f == 0:
                        print(x,y,z,w,u)