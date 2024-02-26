from turtle import*
speed(0)
k = 40
cnt = 0
begin_fill()
for i in range(3):
    right(45)
    forward(10*k)
    right(45)
right(315)
forward(10*k)
for i in range(2):
    right(90)
    forward(10*k)
end_fill()
canvas = getcanvas()
for x in range(-100,100):
    for y in range(-100,100):
        if canvas.find_overlapping(x*k,y*k,x*k,y*k) == (5,):
            cnt += 1
print(cnt)
done()