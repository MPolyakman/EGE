import turtle
from turtle import*
cnt1 = 0
cnt2 = 0
cnt3 = 0
color('black','red')
speed(0)
k = 40
cnt = 0
canvas = getcanvas()
begin_fill()
left(90)
begin_fill()
for i in range(2):
    forward(16*k)
    right(90)
    forward(9*k)
    right(90)
turtle.up()
end_fill()
forward(5*k)
right(90)
forward(11*k)
right(90)
turtle.down()
begin_fill()
for i in range(2):
    forward(20*k)
    right(90)
    forward(8*k)
    right(90)
end_fill()

canvas = getcanvas()
for x in range(-100,100):
    for y in range(-100,100):
        print(canvas.find_overlapping(x*k,y*k,x*k,y*k))
        # if 5 in canvas.find_overlapping(x*k,y*k,x*k,y*k) or 4 in canvas.find_overlapping(x*k,y*k,x*k,y*k):
            # cnt1 += 1
        if 7 in canvas.find_overlapping(x*k,y*k,x*k,y*k) or 6 in canvas.find_overlapping(x*k,y*k,x*k,y*k) or\
                2 in canvas.find_overlapping(x*k,y*k,x*k,y*k) or 3 in canvas.find_overlapping(x*k,y*k,x*k,y*k):
            cnt1 += 1
        if (5 in canvas.find_overlapping(x*k,y*k,x*k,y*k) and 7 in canvas.find_overlapping(x*k,y*k,x*k,y*k)) or\
            (5 in canvas.find_overlapping(x*k,y*k,x*k,y*k) and 6 in canvas.find_overlapping(x*k,y*k,x*k,y*k)):
            cnt2 += 1
        if 7 in canvas.find_overlapping(x*k,y*k,x*k,y*k) and 4 in canvas.find_overlapping(x*k,y*k,x*k,y*k):
            cnt3 += 1
print(cnt1 - cnt2 + cnt3)
done()

