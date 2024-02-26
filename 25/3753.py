for number in range(113*(10**6),114*(10**6)+1):
    divs = []
    for div in range(2,int(number**0.5)+1,2):
        if number % div:
            print('BRUH')
        