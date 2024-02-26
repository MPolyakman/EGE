print("x y z w f")
for x in range (2):
    for y in range (2):
        for z in range (2):
            for w in range (2):
                f = (w or x or y) <= ((y or z) and x or y and (w or z))
                if f == 0:
                    print(x,y,z,w,f)
# y ,w  z, ,x