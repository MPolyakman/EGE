answer = []
answer2 = []
for i in range(10000,31623):
    number = i**2
    divs = []
    for div in range(1,i+1):
        if number%div == 0:
            divs.append(div)
            if div != number // div:
                divs.append(number // div)
        if len(divs) > 39:
            break
    if len(divs) == 39:
        print(number, max(div for div in divs if div%2 != 0))
