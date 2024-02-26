for number in range(174457,174506):
    divs = []
    for div in range(2,number):
        if number % div == 0:
            divs.append(div)
    if len(divs) == 2:
        print(divs[0],divs[1],divs[0]*divs[1])