import turtle
from turtle import*
speed(0)
left(90)
k = 40
cnt = 0
begin_fill()
for i in range(2):
    forward(13*k)
    right(90)
    forward(20*k)
    right(90)
turtle.up()
end_fill()
forward(8*k)
right(90)
back(3*k)
left(90)
begin_fill()
turtle.down()
for i in range(2):
    forward(16*k)
    right(90)
    forward(8*k)
    right(90)
end_fill()
canvas = getcanvas()
for x in range(-100,100):
    for y in range(-100,100):
        if canvas.find_overlapping(x*k,y*k,x*k,y*k) != ():
            cnt += 1
        print(canvas.find_overlapping(x * k, y * k, x * k, y * k))

print(cnt)
done()

