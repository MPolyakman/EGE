cymma = 0
for x in range (71):
    for y in range (81):
        a = 2*(71**3) + x*(71**2) + x*(71**1) + 3*(71**0)
        b = 4*(73**3) + 8*(73**2) + x*(73**1) + 4*(73**0)
        c = 7*(78**3) + x*(78**2) + 6*(78**1) + 5*(78**0)
        d = 3*(81**3) + x*(81**2) + y*(81**1) + 9*(81**0)
        summ = a + b + c - d
        if summ > 0 and summ % 1234 == 0:
            cymma += x + y
print(cymma)