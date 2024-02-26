for number in range(126849,126872):
    divs = []
    for div in range(1,int(number**0.5)+1):
        if number % div == 0:
            divs.append(div)
            if div != number//div:
                divs.append(number//div)
    if len(divs) == 4:
        divs.sort()
        print(divs[-2],number)