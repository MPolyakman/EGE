answer = 0
for number in range(500001,1000000):
    divsum = []
    for div in range(1,int(number**0.5)+1):
        if number % div == 0:
            divsum.append(div)
            if div != number//div:
                divsum.append(number//div)
    if str(sum(divsum))[-2] == '7':
        print(number, sum(divsum))
        answer += 1
    if answer == 5:
        break

