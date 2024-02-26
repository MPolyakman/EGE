from turtle import*
down()
k = 10
speed(0)
cnt = 0
for i in range(10):
    left(90)
    forward(2*k)
    right(90)
    forward(2*k)
    begin_fill()
    left(90)
    forward(10*k)
    left(90)
    forward(2*k)
    right(90)
    forward(2*k)
    right(90)
    forward(6*k)
    right(90)
    forward(2*k)
    right(90)
    forward(2*k)
    left(90)
    forward(10*k)
    right(90)
    forward(2*k)
    end_fill()
    right(90)
    forward(2*k)
    right(90)
    forward(6*k)
canvas = getcanvas()
for x in range(-100,100):
    for y in range(-100,100):
        if 5 in canvas.find_overlapping(x*k,y*k,x*k,y*k):
            cnt += 1
print(cnt)
done()

