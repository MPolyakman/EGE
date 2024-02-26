from turtle import*
k = 100
cnt = 0
speed(0)
left(90)
begin_fill()
for i in range(3):
    left(90)
    for i in range(4):
        forward(5*k)
        right(90)
end_fill()
canvas = getcanvas()
for x in range(-100,100):
    for y in range(-100, 100):
        if 5 in canvas.find_overlapping(x*k,y*k,x*k,y*k):
            cnt += 1
print(cnt)
done()
#аналитикой