import turtle
from turtle import*
k = 10
cnt = 0
speed(0)
left(90)
for x in range(100,10000):
    begin_fill()
    for i in range(4):
        forward(3*x*k)
        right(90)
    turtle.up()
    end_fill()
    forward(x*k)
    right(90)
    forward(x*k)
    begin_fill()
    turtle.down()
    for i in range(4):
        forward(x*k)
        left(90)
    end_fill()
    canvas = getcanvas()
    for x in range(-100,100):
        for y in range(-100, 100):
            if (canvas.find_overlapping(x*k,y*k,x*k,y*k,)) == (5,):
                cnt += 1
    if cnt > 10**6:
        print(x)
    else:
        cnt = 0
done()