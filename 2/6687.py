print('x y z w f')
for x in range(0,2):
    for y in range(0,2):
        for z in range(0, 2):
            for w in range(0, 2):
                f = (x and y) or (y == z) or w
                if f == 0:
                    print(x, y, z, w, f)
# z,y ,w ,x