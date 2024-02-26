from turtle import*
speed(0)
k = 40
left(90)
index = 3
for i in range(1,100):
    index += 2
    begin_fill()
    cnt = 0
    for m in range(4):
        forward(i*k)
        right(90)
        forward(i*k)
        left(90)
        forward(i*k)
        right(90)
    end_fill()
    canvas = getcanvas()
    for x in range(-100,100):
        for y in range(-100, 100):
            # print(canvas.find_overlapping(x * k, y * k, x * k, y * k))
            if index in canvas.find_overlapping(x*k,y*k,x*k,y*k):
                cnt += 1
    print(i, cnt)
    if cnt > 1000:
        print(i, '<== OTBET')
        break
    clear()

done()