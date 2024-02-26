from fnmatch import*
cnt = 0
for number in range(65001,1000000):
    if fnmatch(str(number),'6*97*5?'):
        divs = []
        for div in range(1,int(number**0.5)+1):
            if number % div == 0:
                divs.append(div)
                if div != number // div:
                    divs.append(number // div)
        if len([i for i in divs if i%2 == 0]) >= 4:
            cnt += 1
            print(number,sum([i for i in divs if i%2 == 0]))
        if cnt > 7:
            break