f = open('17_10100.txt')
widest = []
numbers = [int(number) for number in f]
biggest = max([number for number in numbers if number % 100 == 13])
for i in range(len(numbers) - 2):
    troika = [numbers[i],numbers[i+1],numbers[i+2]]
    cnt_3 = 0
    yslovie = 0
    for n in troika:
        if len(str(n)) == 3:
            cnt_3 +=1
    if sum(troika) <= biggest:
        yslovie += 1
    if cnt_3 == 2 and yslovie == 1:
        widest.append(sum(troika))
print(len(widest),max(widest))
