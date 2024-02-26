f = open('17_12926.txt')
numbers = [int(number) for number in f]
big2 = max([number for number in numbers if len(str(abs(number))) == 2])
a = []
answer = []
for i in range(len(numbers)-3):
    four = [numbers[i], numbers[i+1], numbers[i+2], numbers[i+3]]
    if str((numbers)[i])[-1] == str(numbers[i+1])[-1] and str(numbers[i])[-1] == str(numbers[i+2])[-1] and str(numbers[i])[-1] == str(numbers[i+3])[-1]:
        a.append(sum(four))
a = max(a)
for i in range(len(numbers)-4):
    cnt = 0
    five = [numbers[i], numbers[i+1], numbers[i+2], numbers[i+3], numbers[i+4]]
    for number in five:
        if number < a:
            cnt += 1
    if cnt == 1 and sum(five)%big2==0:
        answer.append(sum(five))
print(len(answer),min(answer))

