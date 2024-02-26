f = open('17-388.txt')
answer = []
numbers = [int(number) for number in f]
biggest = max(int(x) for x in numbers if str(abs(x))[-2:] == '68')
for i in range(len(numbers)-3):
    quatro = [numbers[i],numbers[i+1],numbers[i+2],numbers[i+3]]
    cnt = 0
    for number in quatro:
        if len(str(abs(number))) == 2:
            cnt += 1
    if (cnt == 1 or cnt == 4) and sum(quatro) >= biggest:
        answer.append(sum(quatro))
print(len(answer),max(answer))