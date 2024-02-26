scislenie = 3
n = int('121',scislenie)
while n != ((int('101',7)) - 1):
    scislenie += 1
    n = int('121',scislenie)
print(scislenie)
x = ''
while scislenie > 0:
    x = str(scislenie % 3) + x
    scislenie = scislenie // 3
print(x)


for x in range(3,37):
    if int('121', x) + 1 == int('101',7):
        otv = ''
        while x > 0:
            otv = str(x % 3) + otv
            x //= 3
print(otv)